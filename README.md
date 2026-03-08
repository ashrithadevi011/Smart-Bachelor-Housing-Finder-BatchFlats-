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

Budget

Profession

Sleep schedule

Food preference

are converted into numerical vectors and compared using Cosine Similarity to find the best matches.

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

#Future Improvements:

Add real-time chat between roommates

Deploy application to cloud platform

Implement image uploads for property listings

Use PostgreSQL for scalable database management

Output:

1. Landing Page
2. A modern, glassmorphism-inspired landing page that allows bachelors to search for broker-free housing by location.

3. <img width="1826" height="853" alt="Screenshot 2026-03-08 050022" src="https://github.com/user-attachments/assets/056c8d77-17e7-4049-b438-7d611c1a80a3" />


