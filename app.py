import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import db, User, Property, Review, RoommatePost, Message
from models.ai_engine import recommend_houses, detect_fake_review, match_roommates
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
db.init_app(app)

with app.app_context():
    db.create_all()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    properties = Property.query.limit(6).all()
    return render_template('index.html', properties=properties)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        role = request.form.get('role')

        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(name=name, email=email, phone=phone, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.user_id
            session['role'] = user.role
            session['name'] = user.name
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if session.get('role') == 'Owner':
        properties = Property.query.filter_by(owner_id=session['user_id']).all()
        return render_template('dashboard_owner.html', properties=properties)
    else:
        # AI Recommendation logic here, assume a mock budget and location since we don't store them in user yet
        # or we could get it from roommate post
        user_post = RoommatePost.query.filter_by(user_id=session['user_id']).first()
        recommendations = []
        if user_post:
            recommendations = recommend_houses(user_post.budget, user_post.location, top_n=3)
        return render_template('dashboard_tenant.html', saved_houses=[], recommendations=recommendations)

@app.route('/properties')
def properties_list():
    location = request.args.get('location')
    if location:
        properties = Property.query.filter(Property.location.contains(location)).all()
    else:
        properties = Property.query.all()
    return render_template('property_list.html', properties=properties)

@app.route('/property/<int:property_id>')
def property_details(property_id):
    property_obj = Property.query.get_or_404(property_id)
    reviews = Review.query.filter_by(property_id=property_id).all()
    return render_template('property_details.html', property=property_obj, reviews=reviews)

@app.route('/property/<int:property_id>/review', methods=['POST'])
@login_required
def add_review(property_id):
    rating = request.form.get('rating')
    comment = request.form.get('comment')
    
    # Fake review detection
    is_suspicious = detect_fake_review(comment)
    
    new_review = Review(
        property_id=property_id,
        user_id=session['user_id'],
        rating=int(rating),
        comment=comment,
        is_suspicious=is_suspicious
    )
    db.session.add(new_review)
    db.session.commit()
    
    if is_suspicious:
        flash('Review submitted, but flagged for manual verification.', 'info')
    else:
        flash('Review submitted successfully!', 'success')
        
    return redirect(url_for('property_details', property_id=property_id))

@app.route('/property/add', methods=['GET', 'POST'])
@login_required
def add_property():
    if session.get('role') != 'Owner':
        flash('Only owners can add properties.', 'danger')
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        image_file = request.files.get('image')
        image_path = ''
        if image_file and image_file.filename:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            image_file.save(image_path)
            image_path = 'images/' + image_file.filename

        new_prop = Property(
            owner_id=session['user_id'],
            title=request.form.get('title'),
            location=request.form.get('location'),
            rent=request.form.get('rent'),
            deposit=request.form.get('deposit'),
            description=request.form.get('description', ''),
            rooms=request.form.get('rooms'),
            furnishing=request.form.get('furnishing'),
            bachelor_allowed=True if request.form.get('bachelor_allowed') == 'on' else False,
            food=True if request.form.get('food') == 'on' else False,
            wifi=True if request.form.get('wifi') == 'on' else False,
            image_path=image_path
        )
        db.session.add(new_prop)
        db.session.commit()
        flash('Property added successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('property_add.html')

@app.route('/roommates', methods=['GET', 'POST'])
def roommates():
    if request.method == 'POST':
        if 'user_id' not in session:
            flash('Please login to post a requirement.', 'danger')
            return redirect(url_for('login'))
            
        new_post = RoommatePost(
            user_id=session['user_id'],
            location=request.form.get('location'),
            budget=request.form.get('budget'),
            profession=request.form.get('profession'),
            food_preference=request.form.get('food_preference'),
            sleep_schedule=request.form.get('sleep_schedule'),
            smoking_preference=request.form.get('smoking_preference')
        )
        db.session.add(new_post)
        db.session.commit()
        flash('Roommate requirement posted!', 'success')
        return redirect(url_for('roommates'))

    all_posts = RoommatePost.query.all()
    matched_posts = []
    
    if 'user_id' in session:
        user_post = RoommatePost.query.filter_by(user_id=session['user_id']).first()
        if user_post and all_posts:
            # Calculate similarity
            try:
                matches = match_roommates(user_post, all_posts)
                # Just show the top posts
                return render_template('roommate.html', posts=all_posts, matches=matches, current_user_post=user_post)
            except Exception as e:
                print("Error matching:", e)
    
    return render_template('roommate.html', posts=all_posts, matches=[])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
