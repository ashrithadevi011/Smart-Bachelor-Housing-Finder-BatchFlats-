# Smart-Bachelor-Housing-Finder-BatchFlats

Smart Bachelor Housing Finder is a full-stack web application designed to help bachelors easily find rental houses and compatible roommates without paying brokerage fees. The platform provides bachelor-friendly property listings, smart roommate matching, and review analysis to improve trust and transparency in rental listings.

#Project Features:
#Property Discovery:

Users can search rental houses based on location. The system displays available listings including rent, furnishing status, and bachelor availability.

#Dynamic Property Filtering:

Users can apply filters such as:

Budget range

Bachelor-friendly houses

WiFi availability

Food included

The backend processes these filters and retrieves matching properties from the database.

#Property Details Page:

Each property has a detailed page displaying:

Property image

Monthly rent

Location

Number of rooms

Furnishing status

WiFi availability

#Description:

The page also includes the property owner's contact section and an embedded map showing the location.

#AI Roommate Matching:

The system recommends compatible roommates using a machine learning algorithm.

#User preferences such as:

Budget, Profession, Sleep schedule and Food preference are converted into numerical vectors and compared using Cosine Similarity to find the best matches.

#Fraud Review Detection:

The platform analyzes user reviews using Natural Language Processing. Sentiment analysis is performed to detect suspicious or fake reviews and prevent manipulation of property ratings.

#Secure Authentication:

The application includes a secure login and registration system with password hashing to protect user credentials.

#Tech Stack:
Backend
Python
Flask
SQLAlchemy ORM
SQLite Database

#Frontend:

HTML
CSS
Jinja2 Templates

#AI / Machine Learning:

Pandas
NumPy
Scikit-Learn (Cosine Similarity)
TextBlob (Sentiment Analysis)


Output:
1. Landing Page:
   A modern, glassmorphism-inspired landing page that allows bachelors to search for broker-free housing by location.

 <img width="1826" height="853" alt="Screenshot 2026-03-08 050022" src="https://github.com/user-attachments/assets/056c8d77-17e7-4049-b438-7d611c1a80a3" />

2. Property Discovery:
     A dynamic gallery of featured listings showing transparent pricing and bachelor-friendly tags for properties across major          tech hubs.

   <img width="432" height="661" alt="Screenshot 2026-03-08 050110" src="https://github.com/user-attachments/assets/6bebec4f-141d-446c-8863-8d108437cbb2" />

3. Smart Search & Filters:
An advanced filtering system that allows users to narrow down homes based on budget ranges and specific amenities like WiFi or food availability.


<img width="952" height="860" alt="Screenshot 2026-03-08 050157" src="https://github.com/user-attachments/assets/9e2d4a3f-2a61-4f46-aaa2-79e26395d17b" />

4. Detailed Property View & Maps:
A comprehensive property detail page integrating location maps and direct owner contact information for seamless inquiries.

<img width="1264" height="802" alt="Screenshot 2026-03-08 050215" src="https://github.com/user-attachments/assets/a7421da4-605b-4239-a163-f11d3ab733a9" />

5. AI-Powered Fraud Detection:
An intelligent review system using Natural Language Processing (NLP) to flag potentially fake or spam reviews, ensuring platform integrity.

<img width="844" height="801" alt="Screenshot 2026-03-08 050238" src="https://github.com/user-attachments/assets/2467befe-5b5f-40cf-ab4e-72fa49e6b9b2" />

6. AI Roommate Matching:
A dedicated roommate portal that uses Scikit-Learn and Cosine Similarity to match users based on lifestyle habits, profession, and budget.

<img width="1118" height="754" alt="Screenshot 2026-03-08 050304" src="https://github.com/user-attachments/assets/d9da237c-f6a8-469d-a836-f60a213c3492" />

7. Secure Authentication:
A secure registration flow that implements role-based access control for tenants and owners while ensuring password safety via PBKDF2 hashing.

Sign Up Page:

<img width="544" height="707" alt="Screenshot 2026-03-08 050319" src="https://github.com/user-attachments/assets/0d4b8a11-c4f5-49c7-91ca-d5c0972e1fb8" />

Login Page:

<img width="448" height="448" alt="Screenshot 2026-03-08 050327" src="https://github.com/user-attachments/assets/55fa17dd-345b-4ce8-8e4c-3bcbfc2f31b1" />


#Revised Folder Structure (Based on your screenshots)

A modular directory layout ensuring a clean separation between backend logic, frontend templates, and static assets.


housing_app/
├── instance/
│   └── database.db         # Local SQLite database file [cite: 8]
├── models/                 # Database schemas and logic [cite: 8]
│   └── ai_engine.py        # AI matching and sentiment analysis logic [cite: 15, 16]
├── static/                 # CSS, JS, and Media assets [cite: 12]
│   ├── images/
│   ├── js/
│   └── videos/
├── templates/              # HTML files powered by Jinja2 [cite: 10, 11]
│   ├── base.html           # Master layout template
│   ├── dashboard_owner.html# Owner-specific dashboard [cite: 24, 25]
│   ├── dashboard_tenant.html # Tenant-specific dashboard [cite: 25]
│   ├── index.html          # Landing page [cite: 13]
│   ├── login.html          # User login page [cite: 33]
│   ├── property_add.html   # Form for owners to list property [cite: 25]
│   ├── property_details.html # Detailed property view [cite: 29]
│   ├── property_list.html  # Main property gallery [cite: 11]
│   ├── register.html       # User registration page [cite: 33]
│   └── roommate.html       # Roommate matching interface [cite: 18, 23]
├── app.py                  # Main Flask application entry point [cite: 1, 7]
├── database.py             # Database configuration [cite: 8, 20]
├── requirements.txt        # Project dependencies [cite: 15, 16]
└── seed_db.py              # Script for initial database population



#Author

Made by Vagmare Ashritha Devi







