from app import app
from database import db, User, Property, Review, RoommatePost
from werkzeug.security import generate_password_hash
from datetime import datetime

def seed_db():
    with app.app_context():
        # Clear existing data safely
        db.drop_all()
        db.create_all()

        # Users
        hashed_password = generate_password_hash("password", method='pbkdf2:sha256')
        
        ashritha = User(name="Ashritha Devi", email="ashritha@example.com", phone="9988776655", password=hashed_password, role="Tenant")
        owner1 = User(name="Ramesh Kumar", email="ramesh@example.com", phone="9988776651", password=hashed_password, role="Owner")
        owner2 = User(name="Suresh Iyer", email="suresh@example.com", phone="9988776652", password=hashed_password, role="Owner")
        tenant1 = User(name="Rahul Sharma", email="rahul@example.com", phone="9988776653", password=hashed_password, role="Tenant")
        tenant2 = User(name="Neha Gupta", email="neha@example.com", phone="9988776654", password=hashed_password, role="Tenant")
        
        db.session.add_all([ashritha, owner1, owner2, tenant1, tenant2])
        db.session.commit()

        # Properties
        prop1 = Property(
            owner_id=owner1.user_id, 
            title="Spacious 2BHK in Gachibowli", 
            location="Gachibowli, Hyderabad", 
            rent=25000, 
            deposit=100000, 
            description="Great apartment for bachelors. Close to tech parks.", 
            rooms=2, 
            furnishing="Semi-Furnished", 
            bachelor_allowed=True, 
            wifi=True, 
            food=False, 
            image_path="images/prop1_kormangala.png"
        )
        prop2 = Property(
            owner_id=owner2.user_id, 
            title="1BHK Studio in Madhapur", 
            location="Madhapur, Hyderabad", 
            rent=18000, 
            deposit=50000, 
            description="Cozy studio near metro station.", 
            rooms=1, 
            furnishing="Fully-Furnished", 
            bachelor_allowed=True, 
            wifi=True, 
            food=True, 
            image_path="images/prop2_indiranagar.png"
        )
        prop3 = Property(
            owner_id=owner1.user_id, 
            title="3BHK Family Flat in Banjara Hills", 
            location="Banjara Hills, Hyderabad", 
            rent=35000, 
            deposit=150000, 
            description="Strictly for families. No bachelors allowed.", 
            rooms=3, 
            furnishing="Unfurnished", 
            bachelor_allowed=False, 
            wifi=False, 
            food=False, 
            image_path="images/prop3_whitefield.png"
        )
        
        prop4 = Property(
            owner_id=owner2.user_id, 
            title="Premium 2BHK in Kormangala", 
            location="Kormangala, Bangalore", 
            rent=28000, 
            deposit=120000, 
            description="Sleek modern design, aesthetic lighting, very chill owner.", 
            rooms=2, 
            furnishing="Fully-Furnished", 
            bachelor_allowed=True, 
            wifi=True, 
            food=False, 
            image_path="images/prop4_hsr.png"
        )

        prop5 = Property(
            owner_id=owner1.user_id, 
            title="Luxury Co-living Space in Adyar", 
            location="Adyar, Chennai", 
            rent=15000, 
            deposit=30000, 
            description="Vibrant colors, modern common area, great community.", 
            rooms=1, 
            furnishing="Fully-Furnished", 
            bachelor_allowed=True, 
            wifi=True, 
            food=True, 
            image_path="images/prop5_marathahalli.png"
        )
        
        db.session.add_all([prop1, prop2, prop3, prop4, prop5])
        db.session.commit()

        # Roommate Posts
        post1 = RoommatePost(
            user_id=ashritha.user_id, 
            location="Gachibowli, Hyderabad", 
            budget=15000, 
            profession="Data Scientist", 
            food_preference="Veg", 
            sleep_schedule="Early Bird", 
            smoking_preference="No"
        )
        post2 = RoommatePost(
            user_id=tenant1.user_id, 
            location="Madhapur, Hyderabad", 
            budget=14000, 
            profession="Software Engineer", 
            food_preference="Any", 
            sleep_schedule="Night Owl", 
            smoking_preference="Yes"
        )
        post3 = RoommatePost(
            user_id=tenant2.user_id, 
            location="Adyar, Chennai", 
            budget=16000, 
            profession="Designer", 
            food_preference="Veg", 
            sleep_schedule="Early Bird", 
            smoking_preference="No"
        )

        db.session.add_all([post1, post2, post3])
        db.session.commit()

        # Reviews
        rev1 = Review(
            property_id=prop1.property_id, 
            user_id=tenant1.user_id, 
            rating=4, 
            comment="Good place, chill owner. Minor maintenance issues but overall fine.", 
            is_suspicious=False
        )
        # Fake review to demonstrate detection
        rev2 = Review(
            property_id=prop1.property_id, 
            user_id=tenant2.user_id, 
            rating=5, 
            comment="THIS IS THE BEST HOUSE EVER! THE OWNER IS AN ANGEL SENT FROM HEAVEN AND THE RENT IS ESSENTIALLY FREE!!!", 
            is_suspicious=True
        ) 
        
        db.session.add_all([rev1, rev2])
        db.session.commit()

        print("Database seamlessly seeded with mock data. 6 users, 5 properties, 3 roommate posts, 2 reviews created.")

if __name__ == '__main__':
    seed_db()
