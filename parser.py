import fitz  # PyMuPDF
import io

def extract_text_from_pdf(uploaded_file):
    pdf_stream = io.BytesIO(uploaded_file.read())
    text = ""
    with fitz.open(stream=pdf_stream, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8")

