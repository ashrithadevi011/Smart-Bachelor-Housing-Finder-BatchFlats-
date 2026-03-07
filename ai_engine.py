import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from database import Property, RoommatePost, Review

def recommend_houses(tenant_budget, tenant_location, top_n=3):
    """
    Given an ideal budget and location, find the best matching houses using KNN logic.
    Here we compute simple distance based on budget.
    """
    properties = Property.query.all()
    if not properties:
        return []
    
    # We will prioritize location match, then budget proximity using a simple heuristic since
    # true KNN needs more numerical features. We'll encode location just by exact string match for a bonus.
    
    data = []
    for p in properties:
        data.append({
            'property_id': p.property_id,
            'rent': p.rent,
            'location': p.location,
            'bachelor_allowed': p.bachelor_allowed
        })
        
    df = pd.DataFrame(data)
    
    # Filter explicitly for bachelor allowed if we want (or handle in query)
    df = df[df['bachelor_allowed'] == True]
    
    if df.empty:
        return []
        
    # Simple score: Difference in budget
    df['budget_diff'] = abs(df['rent'] - tenant_budget)
    
    # Sort by location match first (boolean 0 or 1), then by budget difference
    df['location_match'] = df['location'].apply(lambda x: 1 if tenant_location.lower() in x.lower() else 0)
    
    df = df.sort_values(by=['location_match', 'budget_diff'], ascending=[False, True])
    
    recommended_ids = df.head(top_n)['property_id'].tolist()
    
    return Property.query.filter(Property.property_id.in_(recommended_ids)).all()

def detect_fake_review(review_text):
    """
    Uses TextBlob to detect if a review might be spam/fake.
    A very generic, extremely polarized sentiment, or repeated spam words can trigger this.
    """
    blob = TextBlob(review_text)
    sentiment = blob.sentiment.polarity
    
    spam_keywords = ['buy', 'crypto', 'fake', 'scam', 'click here', 'invest', 'bitcoin']
    
    if any(keyword in review_text.lower() for keyword in spam_keywords):
        return True
        
    # If the review is perfectly positive (+1.0) and very short, maybe suspicious
    if sentiment == 1.0 and len(review_text.split()) < 3:
        return True
        
    # For now, it's mostly word-based
    return False

def match_roommates(target_post, all_posts):
    """
    Given a target roommate post, find compatible posts using Cosine Similarity on encoded features.
    Features: budget, profession(encoded), sleep_schedule(encoded), food_preference(encoded)
    """
    if not all_posts:
        return []
        
    posts = [target_post] + [p for p in all_posts if p.post_id != target_post.post_id]
    
    data = []
    for p in posts:
        data.append({
            'post_id': p.post_id,
            'budget': p.budget,
            'profession': p.profession,
            'food': p.food_preference,
            'sleep': p.sleep_schedule
        })
        
    df = pd.DataFrame(data)
    
    # Categorical encoding
    df = pd.get_dummies(df, columns=['profession', 'food', 'sleep'])
    
    # Normalize budget (Min-Max)
    max_b = df['budget'].max()
    min_b = df['budget'].min()
    if max_b > min_b:
        df['budget'] = (df['budget'] - min_b) / (max_b - min_b)
    else:
        df['budget'] = 1.0
        
    features = df.drop(columns=['post_id']).values
    
    # Target is index 0
    similarities = cosine_similarity([features[0]], features)[0]
    
    # Map back to post_id with score
    results = []
    for i in range(1, len(posts)):
        results.append({
            'post': posts[i],
            'score': round(similarities[i] * 100) # Convert to percentage
        })
        
    # Sort by descending score
    results.sort(key=lambda x: x['score'], reverse=True)
    return results
