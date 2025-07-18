import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

def parse_price(price_data):
    """
    Extract and convert price to float from SerpAPI data (either dict or string).
    Filters out obviously wrong or junk entries (< ₹50).
    """
    if isinstance(price_data, dict):
        price = price_data.get("value", 0)
        try:
            return float(price) if float(price) >= 50 else 0.0
        except (ValueError, TypeError):
            return 0.0
    elif isinstance(price_data, str):
        match = re.search(r"[\d,]+(?:\.\d+)?", price_data)
        if match:
            price_str = match.group(0).replace(",", "")
            try:
                price = float(price_str)
                return price if price >= 50 else 0.0
            except ValueError:
                return 0.0
    return 0.0

def search_products(query, num=5):
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_shopping",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": num,
        "gl": "in",  # 🌏 Country: India
        "hl": "en",  # 🗣️ Language: English
        "google_domain": "google.co.in",  # 📍 Google India domain
    }

    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"[Error] Failed to fetch data from SerpAPI: {e}")
        return []

    results = []
    for item in data.get("shopping_results", []):
        price = parse_price(item.get("price", {}))
        if price == 0.0:
            continue  # Skip invalid or junk price entries

        results.append({
            "title": item.get("title", "").strip(),
            "price": price,
            "store": item.get("source", "").strip(),
            "link": item.get("link", "").strip(),
            "thumbnail": item.get("thumbnail", ""),
            "snippet": item.get("snippet", "").strip()
        })

    return results
