# parser.py
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import pdfplumber
import docx2txt
import pytesseract
from PIL import Image
import os


def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)


def extract_text_from_image(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)


def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext in [".docx", ".doc"]:
        return extract_text_from_docx(file_path)
    elif ext in [".jpg", ".jpeg", ".png"]:
        return extract_text_from_image(file_path)
    else:
        print(f"[⚠️] Unsupported file format: {ext}")
        return ""
