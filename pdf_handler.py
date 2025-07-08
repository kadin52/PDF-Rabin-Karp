from PyPDF2 import PdfReader
from pathlib import Path

def load_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        title = Path(file_path).name
        for page in reader.pages:
            text += page.extract_text()
    return text, title