# 📚🤖 AI Knowledge Base Assistant

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/langchain-powered-orange)](https://github.com/langchain-ai/langchain)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🧠 About

**AI Knowledge Base Assistant** is a conversational tool that lets you **ask questions about your own documents** (PDFs, text files, policies, manuals) using:
- 🔹 [LangChain](https://github.com/langchain-ai/langchain) tool-based agents
- 🔹 Google Gemini embeddings & chat models
- 🔹 Local vector search (FAISS)

Ideal for small teams, internal documentation, or learning how to build retrieval-augmented chat.

---

## ⚙️ How it works

✅ Load your documents → splits them into chunks  
✅ Creates an **embedding index** using Gemini  
✅ Ask questions → retrieves & summarizes answers with source references

---

## 📂 Project Structure

```

ai-knowledge-base-assistant/
├── main.py                # Runs the assistant loop
├── tools.py               # Tools to load & search documents
├── assistant\_output.py    # Structured output model
├── data/                  # Put your PDFs or text files here
├── vector\_store/          # Saved embeddings index
└── requirements.txt       # Dependencies

````

---

## 🚀 Getting Started

1️⃣ **Clone the project**
```bash
git clone https://github.com/Bayzid03/ai-knowledge-base-assistant.git
cd ai-knowledge-base-assistant
````

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Add documents**
Put your PDFs or `.txt` files into the `data/` folder.
Example test file: [letter.pdf]

4️⃣ **Run the assistant**

```bash
python main.py
```

---

## 💡 Sample Usage

```text
You: Load company documents
```

**Assistant output:**

```
Answer:
Loaded 10 text chunks and created vector index.
Sources: data/letter.pdf
```

```text
You: What is this letter about?
```

**Assistant output:**

```
Answer:
Found answer based on docs: This is a sample letter written for demonstration purposes...

Sources:
data/letter.pdf
```

---

## ✏️ Customize

* Add or replace files in `data/`
* Adjust chunk size & embedding settings in `tools.py`
* Extend with more tools (e.g., summary, export)

---

## 📄 License

MIT License — free to use and modify.

---

⭐️ **If you like this project, please star it — it helps!**
*Built with ❤️ using LangChain & Google Gemini*
