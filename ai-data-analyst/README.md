# AI Data Analyst Agent

An AI-powered data analyst agent built with [Langchain](https://github.com/langchain-ai/langchain) and [Gemini](https://ai.google.dev/gemini-api/docs/overview), designed for rapid, explainable analysis of CSV datasets.  
This project enables you to query, analyze, and visualize your data using natural language—no SQL or coding required.

---

Project Status: Under active development. Not yet complete.

## ✨ Features

| Feature                        | Why It Matters                                    | Implementation                                      |
|---------------------------------|---------------------------------------------------|-----------------------------------------------------|
| **Anomaly & Trend Detection**   | Flags revenue drops or spikes automatically       | Tool runs simple statistical checks                 |
| **Explain-your-work JSON Output** | Reproducibility & front-end integration           | Pydantic schema with `answer`, `chart_path`, `query_sql` |
| **Extensibility (new datasets)** | Plug in more CSVs, databases, or APIs             | Keep data access logic in tools only                |

---

## 📁 Project Structure & Why

```
ai-data-analyst/
├── main.py         # Chat loop + agent executor
├── tools.py        # Data, SQL, chart, log tools
├── schema.py       # Output model
├── data/           # CSVs or SQLite DB
│   └── sales.csv
├── charts/         # Auto-generated PNGs
├── logs/           # Chat transcripts
├── requirements.txt
└── .env            # API keys / DB URI
```

- **Why local CSV first?**  
  Rapid iteration with no DB creds; swap to Postgres or BigQuery later by editing `tools.py`.

---

## 🚀 Getting Started

1. **Clone the repo and install dependencies:**
    ```sh
    python -m venv venv
    source venv/bin/activate        # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

2. **Add your API keys to `.env`**  
   (e.g., Gemini API key, DB URI if needed)

3. **Place your CSV data in the `data/` folder.**

4. **Run the agent:**
    ```sh
    python main.py
    ```

---

## 🛠️ Extending

- Add new tools or swap data sources by editing