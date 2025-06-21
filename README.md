# Smart Research Summarizer

An AI-powered assistant that reads, understands, and questions research papers or technical documents (PDF/TXT).

##  Features
- Upload and parse PDF or TXT
- Auto summary (≤ 150 words)
- Ask-anything Q&A with context from document
- Logic-based question generation and evaluation
- Justification for every answer

## How to Run
1. Install dependencies:
```bash
 python -m pip install -r requirements.txt

2. Run Program 
```bash
python -m streamlit run app.py

## Folder Structure

smart-assistant/
├── app.py 
├── backend/
│ ├── logic.py
│ ├── parser.py 
├── utils/
│ └── openai_helpers.py 
├── .env 
├── requirements.txt 
└── README.md 
