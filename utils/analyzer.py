import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    skills = []
    for token in nlp(text):
        if token.pos_ == "NOUN":
            skills.append(token.text)
    return list(set(skills))

def calculate_ats_score(resume_text, job_description):
    documents = [resume_text, job_description]
    tfidf = TfidfVectorizer(stop_words="english")
    vectors = tfidf.fit_transform(documents)
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)
