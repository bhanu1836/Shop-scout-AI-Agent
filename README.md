mkdir -p ShopScout-AI && cd ShopScout-AI

cat << 'EOF' > README.md
# 🛒 ShopScout AI: Multi-Agent Smart Buyer

ShopScout AI is a GenAI-powered product comparison tool built with multi-agent logic. You simply input a product name and budget, and the agent intelligently searches **Google Shopping (India)** using SerpAPI, filters valid products, and returns the **best available deals in INR (₹)** from popular stores like **Amazon.in** and **Flipkart**.

---

## 🚀 Features
- 🔍 Intelligent product search with SerpAPI
- 🇮🇳 India-specific results with accurate ₹ prices
- 📦 Filters out irrelevant or super-cheap items
- 📊 Clean structured output with title, price, store, and snippet
- 🧠 Ready for LLM integration (explanation or summarization agents)
- 💡 Built with modular code structure

---

## 🛠️ Tech Stack
- 🐍 Python
- 🌐 SerpAPI (`google_shopping` engine)
- 🔎 BeautifulSoup + Requests
- 🧪 Optional: Langchain / Ollama (for LLMs)
- 🌱 Streamlit frontend (optional UI)
- 🔐 .env file for API key

---

## 📁 Project Structure

\`\`\`
ShopScout-AI/
├── app.py               # Main app logic (e.g., UI/CLI)
├── agents.py            # AI agent logic (decision making, filtering)
├── scraper.py           # Google Shopping product search via SerpAPI
├── .env                 # Contains your SERPAPI_API_KEY
├── requirements.txt     # Python dependencies
└── README.md
\`\`\`

---

## 🧪 Example Output

\`\`\`
Realme Narzo N65 5G - ₹11499 [Amazon.in]
boAt Rockerz 255 ANC - ₹1499 [Flipkart]
Samsung Galaxy M14 - ₹10999 [Amazon.in]
\`\`\`

---

## 🧾 How to Use

1. **Clone the repo**:
   \`\`\`bash
   git clone https://github.com/yourusername/ShopScout-AI.git
   cd ShopScout-AI
   \`\`\`

2. **Install dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Set up \`.env\` file**:
   \`\`\`
   SERPAPI_API_KEY=your_serpapi_key_here
   \`\`\`

4. **Run the app** (CLI or Streamlit):
   \`\`\`bash
   python app.py
   # OR
   streamlit run app.py
   \`\`\`

---

## 🧠 Future Enhancements
- LLM-based deal justification agent
- Flipkart API scraper or Selenium automation
- Brand filters and spec comparisons
- Voice-based input using Whisper
- Browser extension version

---

## 📜 License
This project is open-sourced under the MIT License.

---

## 👨‍💻 Author
**K. Bhanu Prakash Reddy**  
Feel free to connect or contribute!

EOF
