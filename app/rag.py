from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

with open("data/knowledge.txt", "r", encoding="utf-8") as f:
    documents = f.readlines()

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents)

def retrieve_context(query):
    query_vec = vectorizer.transform([query])
    similarities = (vectors @ query_vec.T).toarray()
    best_idx = np.argmax(similarities)
    return documents[best_idx]