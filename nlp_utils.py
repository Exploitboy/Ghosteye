
import spacy
from sentence_transformers import SentenceTransformer, util

nlp = spacy.load("en_core_web_sm")
transformer_model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_keywords(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

def get_sentence_embedding(text):
    return transformer_model.encode(text, convert_to_tensor=True)

def get_cosine_similarity(text1, text2):
    emb1 = get_sentence_embedding(text1)
    emb2 = get_sentence_embedding(text2)
    return float(util.cos_sim(emb1, emb2).item())