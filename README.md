# 🏠 AI DDR Report Generator

An AI-powered tool that analyzes building inspection and thermal reports (PDFs) and automatically generates a structured **Detailed Diagnostic Report (DDR)** using Google Gemini AI.

---

## 📌 What It Does

Upload two PDF reports — a **Building Inspection Report** and a **Thermal Report** — and the system will:

1. Extract all text and images from both PDFs
2. Send the extracted text to Google Gemini AI
3. Generate a structured **Detailed Diagnostic Report (DDR)** covering:
   - Property Issue Summary
   - Area-wise Observations
   - Probable Root Cause
   - Severity Assessment (with reasoning)
   - Recommended Actions
   - Additional Notes
   - Missing or Unclear Information
4. Display the report and extracted images in a clean Streamlit UI

---

## 🗂️ Repository Structure

```
├── backend/
│   ├── .env                  # Environment variables (API keys)
│   ├── extractor.py          # PDF text and image extractor (PyMuPDF)
│   ├── llm.py                # Gemini AI integration & DDR prompt
│   ├── main.py               # FastAPI server with /generate-ddr endpoint
│   └── images/               # Auto-generated folder for extracted PDF images
│
├── frontend/
│   └── app.py                # Streamlit UI for uploading PDFs & viewing report
│
└── requirements.txt          # Python dependencies
```

---

## 🔄 Application Flow

```
User (Browser)
    │
    │  Uploads inspection.pdf + thermal.pdf
    ▼
Streamlit Frontend (frontend/app.py)
    │
    │  POST /generate-ddr  (multipart form with both PDFs)
    ▼
FastAPI Backend (backend/main.py)
    │
    ├──► extractor.py  →  Extracts text & images from each PDF (PyMuPDF)
    │
    └──► llm.py        →  Sends extracted text to Google Gemini AI
                              │
                              ▼
                         Gemini returns structured DDR text
    │
    │  Returns { report: "...", images: [...] }
    ▼
Streamlit Frontend
    │
    ▼
Displays DDR Report + Extracted Images to User
```

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.9 or higher
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

---

### 1. Clone the Repository

```bash
# Clone your empty repo
git clone https://github.com/Chaitanyasalunkhe17/DDR-AI.git
cd ai-ddr-report-generator
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file inside the `backend/` folder:

```bash
# backend/.env
GEMINI_API_KEY=your_gemini_api_key_here
```

> ⚠️ **Never commit your `.env` file to GitHub.** Add it to `.gitignore`.

---

### 5. Run the Backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload
```

The API will be available at: `http://localhost:8000`

You can explore the auto-generated API docs at: `http://localhost:8000/docs`

---

### 6. Run the Frontend (Streamlit)

Open a **new terminal**, then:

```bash
cd frontend
streamlit run app.py
```

The UI will open in your browser at: `http://localhost:8501`

---

## 🚀 Usage

1. Open the Streamlit app in your browser
2. Upload the **Inspection Report PDF** using the first uploader
3. Upload the **Thermal Report PDF** using the second uploader
4. Click **"Generate DDR"**
5. Wait for the AI to process — the full DDR report and extracted images will appear on the page

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| `fastapi` | 0.110.0 | Backend REST API framework |
| `uvicorn` | 0.29.0 | ASGI server for FastAPI |
| `python-multipart` | 0.0.9 | File upload handling |
| `pymupdf` | 1.24.1 | PDF text & image extraction |
| `google-generativeai` | 0.5.4 | Google Gemini AI client |
| `streamlit` | 1.33.0 | Frontend web UI |
| `requests` | 2.31.0 | HTTP calls from frontend to backend |
| `python-dotenv` | 1.0.1 | Load `.env` variables |

---

## 🔒 Security Notes

- **Do not commit your `.env` file.** Add `backend/.env` to your `.gitignore`.
- The Gemini API key in the repository has been exposed — **regenerate it immediately** in [Google AI Studio](https://aistudio.google.com/app/apikey).

---

## 📄 API Reference

### `POST /generate-ddr`

Accepts two PDF files and returns a structured DDR report.

**Request (multipart/form-data):**

| Field | Type | Description |
|---|---|---|
| `inspection` | PDF file | Building inspection report |
| `thermal` | PDF file | Thermal imaging report |

**Response (JSON):**

```json
{
  "report": "1. Property Issue Summary\n...",
  "images": ["images/page0_img0.png", "images/page0_img1.png", "..."]
}
```

---

## 🛠️ Future Improvements

- Support for more AI providers (OpenAI, Anthropic Claude)
- Export DDR as a downloadable PDF
- Authentication for API access
- Docker support for easy deployment
- Store reports in a database for history

---

## 📃 License

This project is open source. Feel free to use and modify it.
