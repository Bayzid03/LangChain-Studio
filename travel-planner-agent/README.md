# ✈️ AI Travel Planner Agent

> **Intelligent travel itinerary generation powered by Google Gemini AI and LangChain**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green?style=flat-square)](https://langchain.com/)
[![Google AI](https://img.shields.io/badge/Google%20AI-Gemini%202.5-orange?style=flat-square)](https://ai.google.dev/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Validation-red?style=flat-square)](https://pydantic.dev/)

## 🎯 Overview

An intelligent travel assistant that creates **personalized multi-day itineraries** using advanced AI. Built with Google Gemini 2.5 Flash and LangChain's agent framework, featuring automatic plan saving and destination recommendations.

### ✨ Key Features

- **🗺️ Smart Itinerary Generation** - Multi-day travel plans with detailed scheduling
- **🎯 Destination Insights** - AI-powered attraction and activity recommendations  
- **💾 Automatic Saving** - Timestamped itinerary storage with organized file structure
- **📊 Structured Output** - Pydantic-validated responses with highlights extraction
- **💬 Interactive Planning** - Conversational interface with chat history
- **⚡ Fast Processing** - Optimized AI parameters for quick travel suggestions

## 🏗️ Architecture

```
User Query → LangChain Agent → Google Gemini AI → Travel Plan → Auto-Save Tool
     ↓                                              ↓
Chat History                                   Structured JSON
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google AI API Key

### Installation

```bash
# Clone repository
git clone https://github.com/Bayzid03/travel-planner-agent.git
cd travel-planner-agent

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

**Example Planning Session:**
```
You: Plan a 3-day trip to Tokyo for culture and food
✈️ Itinerary: Day 1: Senso-ji Temple, Asakusa district...
🎯 Highlights: Traditional temples, authentic ramen, cherry blossoms
💾 Saved Path: plans/tokyo_20250726_143015.txt
```

## 🛠️ Technical Implementation

### **Core Components**

| Component | Technology | Purpose |
|-----------|------------|---------|
| **AI Engine** | Google Gemini 2.5 Flash | Natural language processing |
| **Agent Framework** | LangChain | Tool orchestration & conversation |
| **Data Validation** | Pydantic | Structured travel plan parsing |
| **File Management** | Custom Tools | Plan persistence & organization |

### **Smart Features**
- **Contextual Planning** - Learns from chat history for personalized suggestions
- **Destination Intelligence** - Built-in knowledge of attractions and activities
- **Automatic Organization** - Location-based file naming with timestamps
- **Error Recovery** - Robust parsing with fallback display options

## 📁 Project Structure

```
travel-planner-agent/
├── main.py           # Application entry point & chat interface
├── schema.py         # Pydantic models for travel plans
├── tools.py          # Plan saving & suggestion tools
├── prompts.py        # AI system prompts & planning guidelines
├── requirements.txt  # Python dependencies
├── .env             # Environment configuration
└── plans/           # Generated itineraries (auto-created)
```

## 🔧 Configuration

### Environment Variables
```env
GOOGLE_API_KEY="your_google_ai_studio_api_key"
```

### Model Parameters
- **Model**: Gemini 2.5 Flash
- **Temperature**: 0.2 (focused, consistent recommendations)
- **Output**: Structured JSON with validation

## 📊 Output Schema

```json
{
  "itinerary": "Detailed multi-day schedule with activities",
  "highlights": "Key experiences and must-see attractions", 
  "saved_path": "File location of saved plan"
}
```

## 🎯 Use Cases

- **Personal Travel Planning** - Custom itineraries for any destination
- **Travel Agency Tools** - Automated plan generation for clients
- **Tourism Education** - Learn about destinations and cultures
- **Business Travel** - Efficient scheduling for work trips

## 🌟 Smart Planning Features

### **Built-in Recommendations**
- 🏛️ Historical landmarks and cultural sites
- 🍜 Traditional cuisine and local dining
- 🎨 Museums and art districts
- 🥾 Outdoor activities and sightseeing
- 🎵 Entertainment and nightlife options

### **Intelligent Organization**
- **Location-based naming** - `tokyo_20250726_143015.txt`
- **Timestamp tracking** - Automatic date/time logging
- **Structured storage** - Organized plans directory
- **Easy retrieval** - Clear file naming conventions

## 🚀 Future Enhancements

- [ ] Budget estimation integration
- [ ] Weather-based recommendations
- [ ] Real-time booking links
- [ ] Multi-language support
- [ ] Mobile app deployment

## 🤝 Contributing

Contributions welcome! Focus areas:
- Additional destination data
- Enhanced recommendation algorithms
- Travel API integrations
- UI/UX improvements

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

**Smart travel planning made simple with AI** 🗺️✨


