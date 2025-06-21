# Smart_Assistant

A GenAI-powered assistant that reads, understands, and reasons over research documents in PDF or TXT format.

##  Features

-  **Document Upload** – Upload PDF or TXT files for analysis.
-  **Auto Summarization** – Instantly generate a concise summary (≤ 150 words).
-  **Ask Anything Mode** – Ask free-form questions grounded in the document content.
-  **Challenge Me Mode** – Answer logic-based questions generated from the document and receive detailed evaluation.
-  **Justified Responses** – Every answer includes source-based justification.
-  **No Hallucinations** – Responses are strictly based on document context.

##  Folder Structure
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
