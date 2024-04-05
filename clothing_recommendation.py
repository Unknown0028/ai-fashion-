from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class ClothingRecommendationSystem:
    def __init__(self):
        # Dummy dataset of clothing items
        self.clothing_data = [
            {"name": "T-shirt", "style": "Casual", "size": "M", "occasion": "Everyday", "price": "$20"},
            {"name": "Dress Shirt", "style": "Formal", "size": "L", "occasion": "Office", "price": "$40"},
            {"name": "Jeans", "style": "Casual", "size": "M", "occasion": "Everyday", "price": "$30"},
            {"name": "Blazer", "style": "Formal", "size": "L", "occasion": "Office", "price": "$60"},
            {"name": "Dress", "style": "Formal", "size": "M", "occasion": "Party", "price": "$50"},
        ]
        self.item_names = [item["name"] for item in self.clothing_data]
        self.item_features = self.extract_features()

    def extract_features(self):
        features = []
        for item in self.clothing_data:
            feature_string = f"{item['style']} {item['size']} {item['occasion']}"
            features.append(feature_string)
        return features

    def recommend(self, user_preferences):
        # Convert user preferences to feature string
        user_preferences_str = ' '.join(user_preferences)
        
        # Compute TF-IDF vectors for both item features and user preferences
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix_items = tfidf_vectorizer.fit_transform(self.item_features)
        tfidf_matrix_user = tfidf_vectorizer.transform([user_preferences_str])

        # Compute cosine similarity between user preferences and item features
        cosine_similarities = linear_kernel(tfidf_matrix_user, tfidf_matrix_items).flatten()

        # Sort items based on similarity scores
        recommendations_indices = cosine_similarities.argsort()[::-1]

        # Get top recommendations
        top_recommendations_indices = recommendations_indices[:3]  # Get top 3 recommendations
        recommendations = [self.clothing_data[idx] for idx in top_recommendations_indices]

        return recommendations

# Example usage
if __name__ == "__main__":
    recommendation_system = ClothingRecommendationSystem()
    user_preferences = ["Casual", "M", "Everyday"]
    recommendations = recommendation_system.recommend(user_preferences)
    if recommendations:
        print("Recommended clothing items:")
        for item in recommendations:
            print(f"Name: {item['name']}, Price: {item['price']}")
    else:
        print("No recommendations found for the given preferences.")
