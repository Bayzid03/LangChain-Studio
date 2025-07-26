# 🩺 AI Symptom Checker Agent

> **Intelligent medical symptom analysis powered by Google Gemini AI and LangChain**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green?style=flat-square)](https://langchain.com/)
[![Google AI](https://img.shields.io/badge/Google%20AI-Gemini%202.5-orange?style=flat-square)](https://ai.google.dev/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Validation-red?style=flat-square)](https://pydantic.dev/)

## 🎯 Overview

An intelligent healthcare assistant that provides **non-diagnostic symptom analysis** using advanced AI. Built with Google Gemini 2.5 Flash and LangChain's agent framework, featuring structured output validation and comprehensive logging.

### ✨ Key Features

- **🤖 AI-Powered Analysis** - Advanced symptom interpretation using Google Gemini 2.5
- **🛡️ Safety-First Design** - Non-diagnostic approach with clear medical disclaimers
- **📊 Structured Output** - Pydantic-validated responses with severity classification
- **💾 Automatic Logging** - Timestamped symptom tracking with tool integration
- **💬 Interactive Chat** - Conversational interface with chat history management
- **⚡ Real-time Processing** - Fast response times with optimized temperature settings

## 🏗️ Architecture

```
User Input → LangChain Agent → Google Gemini AI → Structured Output → Logging Tool
     ↓                                                    ↓
Chat History                                        JSON Response
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google AI API Key

### Installation

```bash
# Clone repository
git clone https://github.com/Bayzid03/symptom-checker-agent.git
cd symptom-checker-agent

# Install dependencies
pip install -r requirements.txt

# Configure API key
# Edit .env file with your Google AI Studio API key
GOOGLE_API_KEY="your_google_api_key_here"
```

### Usage

```bash
python main.py
```

**Example Interaction:**
```
You: I have a headache and feel tired
🧺 Possible Cause: Stress, dehydration, or lack of sleep
🧺 Severity Level: mild
🧺 Advice: Rest, hydrate, and monitor symptoms
🧺 Log: Symptom logged at 2025-07-26 14:30:15
```

## 🛠️ Technical Implementation

### **Core Components**

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI Engine** | Google Gemini 2.5 Flash | Natural language processing |
| **Agent Framework** | LangChain | Tool orchestration & chat management |
| **Data Validation** | Pydantic | Structured output parsing |
| **Logging System** | Custom Tool | Symptom tracking & persistence |

### **Safety Features**
- **Non-diagnostic responses** - Avoids medical diagnoses
- **Severity classification** - Structured risk assessment (mild/moderate/severe)
- **Professional disclaimers** - Clear guidance on medical consultation
- **Input validation** - Robust error handling and parsing

## 📁 Project Structure

```
symptom-checker-agent/
├── main.py           # Application entry point & chat interface
├── schema.py         # Pydantic models for structured output
├── tools.py          # Logging tool implementation
├── prompts.py        # AI system prompts & safety guidelines
├── requirements.txt  # Python dependencies
├── .env             # Environment configuration
└── logs/            # Generated symptom logs (auto-created)
```

## 🔧 Configuration

### Environment Variables
```env
GOOGLE_API_KEY="your_google_ai_studio_api_key"
```

### Model Parameters
- **Model**: Gemini 2.5 Flash
- **Temperature**: 0.3 (balanced creativity/consistency)
- **Max Tokens**: 1000 (optimized for medical responses)

## 📊 Output Schema

```json
{
  "probable_cause": "Potential trigger or cause",
  "severity": "mild | moderate | severe",
  "advice": "Recommended next steps",
  "log_status": "Logging confirmation"
}
```

## 🎯 Use Cases

- **Personal Health Tracking** - Log and analyze symptoms over time
- **Healthcare Education** - Learn about common symptom patterns  
- **Triage Assistance** - Initial severity assessment for healthcare decisions
- **Research Applications** - Symptom data collection and analysis

## 🛡️ Disclaimer

This tool provides **informational guidance only** and is not a substitute for professional medical advice. Always consult qualified healthcare providers for medical concerns.

## 📈 Future Enhancements

- [ ] Symptom history analytics
- [ ] Integration with health APIs
- [ ] Multi-language support
- [ ] Web interface deployment

## 🤝 Contributing

Contributions welcome! Focus areas:
- Enhanced safety validations
- Additional logging features  
- UI/UX improvements
- Medical knowledge base expansion

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

**Built with modern AI technology for responsible healthcare assistance** 🏥✨
