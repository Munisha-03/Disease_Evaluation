# 🩺 Disease LLM API

An AI-powered medical information API built using **FastAPI**, **LangChain**, and **Google Gemini**. This project verifies whether a given input is a valid disease name and, if valid, returns structured, general medical information such as symptoms, causes, diagnosis, treatment, and prevention.

> ⚠️ **Disclaimer**: This API provides **general medical information only** and is **not a substitute for professional medical advice, diagnosis, or treatment**.

---

## 🚀 Features

- ✅ Disease name validation using LLM
- 📋 Structured medical information using Pydantic schemas
- ⚡ FastAPI-based REST API
- 🧠 Google Gemini (LLM) integration via LangChain
- 🔐 Secure environment variable handling
- 🧩 Clean, modular project structure (no circular imports)

---

## 🛠 Tech Stack

- **Backend**: FastAPI & Streamlit
- **LLM Framework**: LangChain
- **LLM Provider**: Google Gemini (`gemini-2.5-flash`)
- **Data Validation**: Pydantic
- **Environment Management**: python-dotenv
- **Language**: Python 3.10+

---

## 📁 Project Structure

```
Disease-llm/
│
├── app.py              # FastAPI entry point
├── streamlit_app.py    # Streamlit Web UI
├── datatypes.py        # Pydantic models
├── parser.py           # LangChain output parsers
├── prompt.py           # Prompt templates
├── main.py             # Core logic & LLM config
├── .env                # Environment variables (not committed)
├── requirements.txt
└── README.md
```

---

## 🔑 Secret Keys & Environment Variables

This project uses **Google Gemini API**. You must set the API key as an environment variable.

### Required Environment Variables

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Disease-llm.git
cd Disease-llm
```

---

### 2️⃣ Create Virtual Environment

#### 🔹 Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

#### 🔹 macOS / Linux

```bash
python3 -m venv myenv
source myenv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

---

### 5️⃣ Run the Application

#### 🔹 Streamlit Web UI (Recommended)
```bash
streamlit run streamlit_app.py
```
The web interface will be available at `http://localhost:8501`.

#### 🔹 FastAPI Backend
```bash
uvicorn app:app --reload
```
The API will start at `http://127.0.0.1:8000`.

---

## 📡 API Endpoints

### 🔹 Health Check

```http
GET /get
```

**Response**

```json
{
  "health_check": "OK"
}
```

---

### 🔹 Get Disease Details

```http
POST /get_disease_details
```

**Request Body**

```json
{
  "disease": "Diabetes"
}
```

**Success Response**

```json
{
  "disease_details": {
    "disease_name": "Diabetes",
    "description": "...",
    "symptoms": [],
    "causes": [],
    "risk_factors": [],
    "diagnosis": "...",
    "treatment": "...",
    "prevention": "..."
  }
}
```

**Invalid Disease Response**

```json
{
  "error": "NOT A DISEASE"
}
```

---

## 🧪 Supported Systems

| System                        | Supported |
| ----------------------------- | --------- |
| Windows 10 / 11               | ✅         |
| macOS (Intel / Apple Silicon) | ✅         |
| Linux (Ubuntu, Debian, Arch)  | ✅         |
| Docker                        | ✅         |

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Author

Built by **Ibrahim Kaleel**\
Software Engineer | AI & Data Science Enthusiast

---

If you need help setting this up or want to extend it further (LangGraph, MCP, production deployment), feel free to ask 🚀

