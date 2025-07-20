import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def ocr_extract_from_pdf(pdf_path, output_txt_path):
    pages = convert_from_path("test_2.pdf", poppler_path=r"C:\Users\Krithika\Desktop\poppler-24.08.0\Library\bin")


    with open(output_txt_path, "w", encoding="utf-8") as output_file:
        for i, page in enumerate(pages):
            text = pytesseract.image_to_string(page)
            output_file.write(f"\n\n--- Page {i+1} ---\n{text}")
    print(f"OCR text saved to {output_txt_path}")

# Run OCR
ocr_extract_from_pdf("test_2.pdf", "output.txt")
