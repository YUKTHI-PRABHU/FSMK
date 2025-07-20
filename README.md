<h1 style="font-size: 48px;">PDF Text Extraction & Prompt Engineering</h1>

 **Introduction**  
 
This project is divided into two main problems:

**Problem 1: PDF Text Extraction**  

Extract clean, readable text from two different types of PDF documents:  

Simple PDFs (digitally generated)

Scanned PDFs (image-based)

The objective is to demonstrate the ability to handle multiple PDF formats using appropriate extraction techniques.

**Problem 2: Prompt Engineering**

Design and iterate effective prompts for large language models (LLMs). This includes:

Identifying core problems

Crafting structured prompts

Testing and refining prompt strategies

---
 **Tools & Libraries:**

**Read PDF**	              -PyMuPDF (fitz), pdfplumber, PyPDF2

**Extract Tables/Images**	 -pdfplumber, tabula-py

**Text Parsing**	         -re (regular expressions)

**OCR (Scanned PDFs)**	    -pytesseract, Pillow, pdf2image

---

 **Installation & Approaches:**

**Text Extraction from Simple PDFs**

**Library Used:** PyMuPDF (fitz)

Installation:
```bash
 pip install pymupdf
```


**OCR for Scanned PDFs**

**Libraries Used:** pytesseract, pdf2image, Pillow

Installation:
```bash
 pip install pytesseract pdf2image pillow
```


Tesseract OCR: Install manually (see below)

---

**Project Structure**
```
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
```
---

** Requirements**
```
pymupdf
pytesseract
pdf2image
Pillow
```


** Text Cleaning Steps**

For Simple PDFs:
```bash
mkdir pdf_extraction
cd pdf_extraction
type nul > pjct.py
```
For creating and activating virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```
Install library:
```bash
pip install pymupdf
```
Run:
```bash
python pjct.py
```
---

For Scanned PDFs:
```bash
mkdir pdf_extraction
cd pdf_extraction
type nul > pjct.py
```
For creating and activating virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```
Install library:
```bash
pip install pytesseract pdf2image pillow
```
Run:
```bash
python pjct.py
```
---
**Challenges Faced & Solutions**

1)Library Compatibility & Setup

Created and used virtual environments for clean installation.

2)Tesseract OCR Installation

 Referred to official and community documentation for guidance.
