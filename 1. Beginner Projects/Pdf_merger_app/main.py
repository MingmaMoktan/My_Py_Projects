# This is my pdf merger app.
from pypdf import PdfWriter

merger = PdfWriter()

pdf_files = []

n = int(input("Enter the number of pdf files you want to merge: "))

for i in range(1, n+1):
    pdf_file_name = input(f"Enter the name of the pdf file {i}: ")
    pdf_files.append(pdf_file_name)

for pdf in pdf_files:
    merger.append(pdf)

merger.write("merged_pdf.pdf")
merger.close()