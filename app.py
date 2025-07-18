import streamlit as st
from agents import search_agent, index_agent, recommend_agent

st.set_page_config(page_title="ShopScout AI", layout="centered")

st.title("🛍️ ShopScout AI – Smart Buyer")

product_name = st.text_input("Product Name", "")
budget = st.number_input("Budget (INR)", min_value=0, step=100, value=5000)
limit = st.slider("Max Results to Consider", min_value=3, max_value=10, value=5)
run_btn = st.button("🔍 Find Best Deal")

if run_btn and product_name:
    with st.spinner("Searching products..."):
        items = search_agent(product_name, budget, limit)
    if not items:
        st.warning("No products found within budget.")
        st.stop()

    st.subheader("✅ Products Within Budget")
    for item in items:
        st.write(f"**{item['title']}** — ₹{item['price']} — {item['store']}")
        st.write(item['link'])
        st.write(item['snippet'])
        st.write("---")

    idx, texts = index_agent(items)

    with st.spinner("Analyzing and recommending..."):
        recommendation = recommend_agent(items, idx, texts, product_name, budget)

    st.subheader("🎯 Best Deal Recommendation")
    st.write(recommendation)
