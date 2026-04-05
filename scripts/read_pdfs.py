import PyPDF2
import sys

def read_pdf(file_path):
    print(f"--- {file_path} ---")
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                print(page.extract_text())
    except Exception as e:
        print(f"Error: {e}")

read_pdf("c:\\Users\\JovanDev\\Desktop\\GABA\\Filosofia Institucional GABA.pdf")
print("\n")
read_pdf("c:\\Users\\JovanDev\\Desktop\\GABA\\Propuesta para Terapeutas Gaba.pdf")
