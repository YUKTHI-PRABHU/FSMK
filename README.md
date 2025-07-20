##Introduction: 
Problem 1: PDF Text Extraction
  Extract clean, readable text from two different types of PDF documents and demonstrate your ability to handle various PDF formats.
Problem 2: Prompt Engineering
  Demonstrate your ability to identify problems, design effective prompts, and iterate on solutions using LLM interactions.

#Tools/Libraries Used:
Read PDF	                 -    PyMuPDF(fitz), pdfplumber, PyPDF2
Extract tables/images      -  	pdfplumber, tabula-py
Data parsing	             -    re (regex)


#Installation /Approches for each PDF type
Text from simple PDF       -	 PyMuPDF (fitz)	pip install pymupdf
OCR for scanned PDF	       -   pytesseract + Pillow + pdf2image	pip install pytesseract pillow pdf2image
Also install Tesseract OCR manually
Save and clean text	Python standard libs


#Project Structure:
YUKTHI-PRABHU/FSMK/
├── Problem-1 Complex Text/
    ├── output.txt
    ___ pjct.py
    ___text_2.pdf
├── Problem-1 Simple Text/
    ├── output.txt
    ___ pjct.py
    ___text_1.pdf
├── Problem-2 Prompt Engineering/
    ___ conversation_links.txt
    ___ final_proposal.txt
    ___implementation_plan.txt
    ___problem_statement.txt
    ___prompt_experiment.txt

#requirements.txt:
pymupdf
pytesseract
pdf2image
Pillow


#Text Cleaning Steps Applied for Simple Text:
mkdir pdf extraction
cd pdf extraction
type nul > pjct.py
Use Virtual Environment :
python -m venv venv
venv\Scripts\activate     
pip install pymupdf
python pjct.py

#Text Cleaning Steps Applied for Complex Text:
mkdir pdf extraction
cd pdf extraction
type nul > pjct.py
Use Virtual Environment :
python -m venv venv
venv\Scripts\activate     
pip install pytesseract
pip install pdf2image pillow
pip install pytesseract pdf2image pillow
python pjct.py

#Installation Steps:
Install Tesseract OCR separately (it's a system tool, not a Python package)
Step-by-step for Windows:
Download Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
Choose the .exe installer (recommended: the one for Windows 64-bit)
During installation:
Select "Add Tesseract to system PATH"
Take note of install location (usually: C:\Program Files\Tesseract-OCR\tesseract.exe)

Install Poppler for Windows and Add to PATH
Install Poppler: https://github.com/oschwartz10612/poppler-windows/releases
Click the latest release, then download the .zip file under "Assets"
Extract the ZIP file :C:\Program Files\poppler-23.11.0\Library\bin
Add this path to your System PATH variable
Press Windows + S → Search Environment Variables
Click “Edit the system environment variables”
In the System Properties window → Click "Environment Variables"
Under System variables, find and edit Path.

##Challenges faced and Solution:
1.working of libraries
  Solution:Created a virtual Environment for the installation of required libararies.
2.Installation of Tesseract OCR
  Solution:Referred  some online resources for the installation procedure.




 






