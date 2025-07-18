import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("paraphrase-MiniLM-L6-v2")

def create_faiss_index(texts):
    embs = MODEL.encode(texts)
    dim = embs.shape[1]
    idx = faiss.IndexFlatL2(dim)
    idx.add(np.array(embs, dtype="float32"))
    return idx

def query_faiss(idx, texts, query):
    q_emb = MODEL.encode([query])
    D, I = idx.search(np.array(q_emb, dtype="float32"), k=3)
    docs = [texts[i] for i in I[0]]
    return docs, D[0]
