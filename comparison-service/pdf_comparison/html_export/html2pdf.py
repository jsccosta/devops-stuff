import fitz  # PyMuPDF

# Specify the path to your HTML file
html_path = "/home/hugo/Desktop/code/silas/dashboard/backend/app/pdf_processing/pdf_comparison/html_export/files/output.html"

# Read the HTML file
with open(html_path, "r") as f:
    html = f.read()

# Create a new PDF
pdf = fitz.open()

# Convert the HTML to PDF
pdf.insert_pdf(fitz.open("html", html))

# Save the PDF
pdf.save("output.pdf")