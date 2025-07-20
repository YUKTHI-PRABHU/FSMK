import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_txt_path):
    doc = fitz.open(pdf_path)
    with open(output_txt_path, "w", encoding="utf-8") as output_file:
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            output_file.write(f"\n\n--- Page {page_num} ---\n")
            output_file.write(text)
    print(f"Text extracted and saved to {output_txt_path}")

pdf_path = "test_1.pdf"           # Replace with your PDF file name
output_txt_path = "output.txt"    # Output file for extracted text
extract_text_from_pdf(pdf_path, output_txt_path)
