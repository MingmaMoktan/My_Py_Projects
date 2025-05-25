# This is my pdf merger app.
"""
If you want to use this app you should install the pypdf by using the following command.

pip install pypdf

And the pdf files that you want to merge should be on the same folder your application file is.
After that you can run the file and enter the number of files you want to merge and enter the names of the pdf files you want to merge. 
And then this will give you the merged pdf file by the default name in the app. 
If you want to change the name of the merged pdf file then you can change the name from the app file.
"""
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