<h1 style="font-size: 48px;">📄 PDF Text Extraction & Prompt Engineering</h1>

 **Introduction**
This project is divided into two main problems:

Problem 1: PDF Text Extraction\n
Extract clean, readable text from two different types of PDF documents:
Simple PDFs (digitally generated)
Scanned PDFs (image-based)
The objective is to demonstrate the ability to handle multiple PDF formats using appropriate extraction techniques.

Problem 2: Prompt Engineering
Design and iterate effective prompts for large language models (LLMs). This includes:
Identifying core problems
Crafting structured prompts
Testing and refining prompt strategies

🧰 Tools & Libraries Used
Task	Tools / Libraries
Read PDF	PyMuPDF (fitz), pdfplumber, PyPDF2
Extract Tables/Images	pdfplumber, tabula-py
Text Parsing	re (regular expressions)
OCR (Scanned PDFs)	pytesseract, Pillow, pdf2image

⚙️ Installation & Approaches
📄 Text Extraction from Simple PDFs
Library Used: PyMuPDF (fitz)

Installation:

bash
Copy
Edit
pip install pymupdf
🖼️ OCR for Scanned PDFs
Libraries Used: pytesseract, pdf2image, Pillow

Installation:

bash
Copy
Edit
```bash
pip install pytesseract pdf2image pillow
Tesseract OCR: Install manually (see below)

🏗️ Project Structure
mathematica
Copy
Edit
YUKTHI-PRABHU/
└── FSMK/
    ├── Problem-1 Complex Text/
    │   ├── text_2.pdf
    │   ├── pjct.py
    │   └── output.txt
    ├── Problem-1 Simple Text/
    │   ├── text_1.pdf
    │   ├── pjct.py
    │   └── output.txt
    ├── Problem-2 Prompt Engineering/
    │   ├── conversation_links.txt
    │   ├── final_proposal.txt
    │   ├── implementation_plan.txt
    │   ├── problem_statement.txt
    │   └── prompt_experiment.txt
📦 requirements.txt
txt
Copy
Edit
pymupdf
pytesseract
pdf2image
Pillow
🧹 Text Cleaning Steps
✅ For Simple PDFs:
bash
Copy
Edit
mkdir pdf_extraction
cd pdf_extraction
type nul > pjct.py

python -m venv venv
venv\Scripts\activate
pip install pymupdf
python pjct.py
✅ For Scanned PDFs:
bash
Copy
Edit
mkdir pdf_extraction
cd pdf_extraction
type nul > pjct.py

python -m venv venv
venv\Scripts\activate
pip install pytesseract pdf2image pillow
python pjct.py
🔧 Additional Installation
🧠 Install Tesseract OCR
Tesseract is not a Python package. It must be installed separately.

Download: Tesseract for Windows (UB Mannheim build)

Choose the Windows 64-bit .exe installer.

During installation:

✔️ Select "Add Tesseract to system PATH"

📁 Note installation path: C:\Program Files\Tesseract-OCR\tesseract.exe

📍 Install Poppler for Windows (required by pdf2image)
Download: Poppler for Windows

Extract the ZIP to a directory like:

makefile
Copy
Edit
C:\Program Files\poppler-23.11.0\Library\bin
Add this path to your System Environment Variables:

Press Windows + S → Search "Environment Variables"

Click "Edit the system environment variables"

In the System Properties window → Click "Environment Variables"

Edit the Path under System Variables and add the Poppler bin path.

🧠 Challenges Faced & Solutions
Library Compatibility & Setup

✅ Created and used virtual environments for clean installation.

Tesseract OCR Installation

✅ Referred to official and community documentation for guidance.
