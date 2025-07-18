from scraper import search_products
from rag_utils import create_faiss_index, query_faiss
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
PROVIDER = "gemini-2.5-pro"

# Agent 1: Search & Scrape
def search_agent(product_name, budget, limit=5):
    items = search_products(product_name, num=limit)
    return [i for i in items if i["price"] <= budget]

# Agent 2: Index for RAG
def index_agent(items):
    texts = []
    for i, x in enumerate(items):
        texts.append(f"Title: {x['title']}. Price: {x['price']}. Store: {x['store']}. Details: {x['snippet']}")
    idx = create_faiss_index(texts)
    return idx, texts

# Agent 3: Competition & Recommendation
def recommend_agent(items, idx, texts, product_name, budget):
    query_text = f"Recommend best deal for '{product_name}' under {budget} rupees."
    docs, _ = query_faiss(idx, texts, query_text)
    top_desc = "\n".join(docs)
    prompt = f"""You are a smart shopping assistant. Given these items:

{top_desc}

Provide:
1. Best product choice with title, price, store, Working link.
2. Comparison to other items (pros/cons).
3. A justification including specs/price/value.
"""
    model = genai.GenerativeModel(PROVIDER)
    resp = model.generate_content([prompt])
    return resp.text
