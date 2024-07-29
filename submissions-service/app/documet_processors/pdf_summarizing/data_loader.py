import os
import fitz  # PyMuPDF


def read_pdf(file_path):
    """
    Read a PDF file and return its content as a single string.

    :param file_path: Path to the PDF file to be read.
    :return: A string containing all the text extracted from the PDF document.
    """
    try:
        pdf_document = fitz.open(file_path)
        extracted_text = ""

        for page_num in range(pdf_document.page_count):
            # Get the page object
            page = pdf_document.load_page(page_num)
            # Extract text from the current page
            page_text = page.get_text()
            extracted_text += page_text

        pdf_document.close()
        return extracted_text
    except Exception as e:
        print(f"Error reading PDF file {file_path}: {e}")
        return None


if __name__ == "__main__":

    test_pdf_directory = os.path.join(os.path.dirname(__file__), 'tests', 'test_files', 'pdf')
    read_pdf(test_pdf_directory)

