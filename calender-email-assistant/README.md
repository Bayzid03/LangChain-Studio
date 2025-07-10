✨ *Calendar & Email Assistant with LangChain & Gemini* ✨

---

# 📅✉️ Calendar & Email Assistant with LangChain & Gemini

An intelligent, AI-powered assistant that helps you **schedule events**, **manage your calendar**, and **handle emails** — all through natural language commands.

Built with:
- 🧠 [LangChain](https://github.com/langchain-ai/langchain) for tool-based agent orchestration
- 🔮 Google Gemini (via `langchain_google_genai`) for conversational AI
- 🛠️ Custom Python tools for calendar & email actions

---

## 🚀 Features
✅ Schedule, reschedule, or cancel calendar events  
✅ Read and summarize unread emails  
✅ Draft emails with recipient, subject, and body  
✅ Structured AI responses using Pydantic  
✅ Interactive CLI interface

---

## 📂 Project Structure
```

project/
├── main.py                # Entry point: runs the assistant
├── tools.py               # Custom tools for calendar & email actions
├── assistant\_output.py    # Pydantic model defining structured assistant response
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables

````

---

## ⚙️ Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/Bayzid03/LangChain-Studio/tree/main
cd calendar-email-assistant
````

2️⃣ **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On Linux/macOS
venv\Scripts\activate      # On Windows
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Add your environment variables**

Create a `.env` file and add your Gemini API key (example):

```ini
GOOGLE_API_KEY=your_api_key_here
```

---

## 🧪 Usage

Run the assistant:

```bash
python main.py
```

Then, interact in natural language:

```text
You: Schedule meeting with Alice tomorrow at 3pm
You: Draft email to bob@example.com about project update
You: Read my unread emails
```

To exit, type: `exit`, `quit`, or `q`.

---

## 📦 Requirements

* Python 3.8+
* [langchain](https://pypi.org/project/langchain/)
* [langchain\_google\_genai](https://pypi.org/project/langchain-google-genai/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [pydantic](https://pypi.org/project/pydantic/)

All included in `requirements.txt`.

---

## ✏️ Customization

* Add more tools in `tools.py` to extend the assistant's capabilities
* Modify the prompt in `main.py` to change the assistant’s personality or instructions

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ⭐️ Support

If you find this project useful, give it a ⭐️ on GitHub — it really helps!

---

*Built with ❤️ using LangChain & Google Gemini.*
