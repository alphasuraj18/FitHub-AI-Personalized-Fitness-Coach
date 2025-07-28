
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class WorkoutRecommender:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.vectorizer = TfidfVectorizer()
        self.goal_vectors = self.vectorizer.fit_transform(self.df['goal'])

    def recommend(self, user_input):
        input_vec = self.vectorizer.transform([user_input])
        similarity = cosine_similarity(input_vec, self.goal_vectors)
        idx = similarity.argmax()
        return self.df.iloc[idx]
