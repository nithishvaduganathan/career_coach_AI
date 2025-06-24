# 🧠 AI Career Coach Chatbot (Flask + LLM)

This is a Python Flask-based AI Career Coach chatbot that uses a Large Language Model (LLM) to provide guidance for career questions. You can ask it things like:

- "How do I become a data scientist?"
- "What are the best certifications for AI?"
- "How to switch careers into machine learning?"

---

## 🚀 Features

- 🔍 Ask career-related questions via a clean web interface
- 🤖 Uses LLM (OpenAI via LangChain) to generate smart answers
- 📚 Embedding-based retrieval from custom career knowledge files
- 🎨 Styled HTML/CSS frontend (Flask + Jinja2)
- 📁 Modular code structure for easy expansion

---

## 🛠️ Technologies Used

- Python
- Flask
- LangChain
- OpenAI API
- FAISS
- HTML + CSS

---

## 📁 Project Structure

```
career_coach_flask/
├── app.py                  # Flask app
├── chatbot_engine.py       # LLM logic using LangChain
├── templates/
│   └── index.html          # Web UI
├── static/
│   └── style.css           # CSS styling
├── knowledge/
│   └── ai_engineer.md      # Sample career guidance knowledge base
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

1. Clone or unzip this project:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

2. Open your browser:
   ```
   http://127.0.0.1:5000
   ```

---

## 🧠 Knowledge Base

All content responses come from files in the `knowledge/` folder.
You can add more `.md` files (e.g. `resume_tips.md`, `career_switch.md`) to expand the bot's knowledge.

---

## 📦 LLM Integration

Currently uses:
- `ChatOpenAI` (OpenAI GPT-3.5/4)
- You need to set your OpenAI API key using:
  ```bash
  export OPENAI_API_KEY=your_key_here
  ```

---

## 🌐 Deployment Options

- Deploy to **Render**, **Railway**, or **Replit**
- Or dockerize for internal use

---

## 📬 Author

Developed by [Your Name]  
This project showcases AI + NLP + Flask integration for practical career guidance.
