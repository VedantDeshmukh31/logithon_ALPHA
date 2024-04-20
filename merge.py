import os
from PyPDF2 import PdfWriter, PdfReader


def merge_pdfs(output_path, *input_paths):
    pdf_writer = PdfWriter()

    for path in input_paths:
        pdf_reader = PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    with open(output_path, "wb") as out:
        pdf_writer.write(out)


# Example usage:
pdf_folder = "pdfs"
output_path = "merged_pdf.pdf"

# List all PDF files in the folder
pdf_files = [
    os.path.join(pdf_folder, filename)
    for filename in os.listdir(pdf_folder)
    if filename.endswith(".pdf")
]

# Merge PDFs
merge_pdfs(output_path, *pdf_files)
