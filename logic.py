from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from utils.openai_helpers import call_openai

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def summarize_text(text):
    prompt = f"Summarize the following document in less than 150 words:\n{text[:3000]}"
    return call_openai(prompt)

def embed_and_index(text):
    chunks = [text[i:i+512] for i in range(0, len(text), 512)]
    embeddings = embedder.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, chunks

def answer_question(question, index, chunks):
    q_embedding = embedder.encode([question])
    D, I = index.search(np.array(q_embedding), k=1)
    context = chunks[I[0][0]]
    prompt = f"Using only the following context, answer the question.\nContext: {context}\nQuestion: {question}"
    answer = call_openai(prompt)
    return answer, context

def generate_questions(text):
    prompt = f"Generate 3 logic-based or inference questions from this document:\n{text[:3000]}"
    raw = call_openai(prompt)
    return raw.strip().split('\n')

def evaluate_response(question, correct_context, user_response):
    prompt = f"Question: {question}\nExpected (based on doc): {correct_context}\nUser Answer: {user_response}\nEvaluate the answer and give justification."
    return call_openai(prompt)
