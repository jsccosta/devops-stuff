import logging
import os
import json
import fitz  # PyMuPDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .data_loader import read_pdf
from .pdf_text_formator import add_text_to_page
from .pdf_processor import (
    preprocess_page_1, preprocess_page_2, preprocess_page_3, preprocess_page_5,
    preprocess_page_6, preprocess_page_7, preprocess_page_8
)
from .data_extractor import (
    extract_info_page_1, extract_info_page_2, extract_info_page_3, extract_info_page_5,
    extract_info_page_6, extract_info_page_7, extract_info_page_8
)


# Configure basic logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_formatted_pdf(pdf_path, output_pdf_path):
    """
    Reads the original PDF, identifies sections based on headers and 
    formats it into a new PDF with each section starting on a new page.

    Parameters:
    - pdf_path: Path to the original PDF file.
    - output_pdf_path: Path where the formatted PDF should be saved.
    """
    
    # Headers used to identify new sections in the PDF
    section_headers = [
        "EXECUTIVE SUMMARY", "ANALYTICS", "BASIC GROUP I", "BASIC GROUP II",
        "LOCATION DETAILS", "BUSINESSES AT ADDRESS", "PROPERTY CHARACTERISTICS"
    ]
    
    # Remove existing output file if it exists
    if os.path.exists(output_pdf_path):
        os.remove(output_pdf_path)
        logging.info(f"Existing file '{output_pdf_path}' has been removed.")

    text_data = read_pdf(pdf_path)
    c = canvas.Canvas(output_pdf_path, pagesize=letter)

    current_section_text = ""
    for line in text_data.split('\n'):
        if line.strip() in section_headers and current_section_text:
            add_text_to_page(c, current_section_text)
            c.showPage()
            current_section_text = line + "\n"
        else:
            current_section_text += line + "\n"

    if current_section_text:
        add_text_to_page(c, current_section_text)

    c.save()
    logging.info(f"Formatted PDF saved as '{output_pdf_path}'.")


def get_recommendations(template):

    template["Recommendation"]["DateOfRecommendation"] = "2/23/2022"
    template["Recommendation"]["Ranking"] = "Critical"
    template["Recommendation"]["Type"] = "Sprinkler Protection"
    template["Recommendation"]["DetailsOfRecommendation"] = "Risk engineer recommendation to implement sprinkler systems throughout premise"
    template["Recommendation"]["ImpactOnLossEstimates"] = "MFL reduction to 30% and NLE reduction to 5%"
    template["Recommendation"]["Status"] = "In progress"
    template["Recommendation"]["ClientComments"] = "Costs for sprinkler implementation being analysed and will be implemented"

    return template


def summarize(pdf_path, output_pdf_path, input_json_path, output_json_path):
    """
    Main function to orchestrate the PDF formatting, preprocessing,
    information extraction, and saving the extracted information into a JSON file.

    Parameters:
    - pdf_path: Path to the original PDF file.
    - output_pdf_path: Path where the formatted PDF will be saved.
    - input_json_path: Path to the input JSON template.
    - output_json_path: Path where the extracted information will be saved as JSON.
    """
    # Format the original PDF and save as a new file
    get_formatted_pdf(pdf_path, output_pdf_path)

    # Open the structured PDF
    doc = fitz.open(output_pdf_path)

    # Load the JSON template
    with open(input_json_path, 'r') as json_file:
        template = json.load(json_file)

    # Define preprocessing and information extraction functions for each page
    preprocess_functions = [
        preprocess_page_1, preprocess_page_2, preprocess_page_3,
        None, preprocess_page_5, preprocess_page_6, preprocess_page_7, preprocess_page_8,
    ]

    extract_info_functions = [
        extract_info_page_1, extract_info_page_2, extract_info_page_3,
        None, extract_info_page_5, extract_info_page_6, extract_info_page_7, extract_info_page_8,
    ]

    # Process each page
    for page_number, page in enumerate(doc):
        if page_number == 3:  # Skip specific pages if needed
            logging.info(f"Skipping page {page_number + 1}")
            continue

        logging.info(f"Processing page {page_number + 1}")
        page_text = page.get_text()

        if preprocess_functions[page_number]:
            processed_text = preprocess_functions[page_number](page_text)
        else:
            processed_text = page_text

        if extract_info_functions[page_number]:
            template = extract_info_functions[page_number](processed_text, template)

    # Get recommendations details
    template = get_recommendations(template)

    # Save the extracted information to a JSON file
    with open(output_json_path, 'w') as json_file:
        json.dump(template, json_file, indent=4)

    logging.info(f"Summary saved to {output_json_path} in JSON format.")

    return template


if __name__ == "__main__":
    
    # Define paths relative to the current file
    base_dir = os.path.dirname(__file__)
    pdf_path = os.path.join(base_dir, 'tests', 'test_files', 'pdf', 'test_pdf1.pdf')
    output_pdf_path = os.path.join(base_dir, 'tests', 'test_files', 'pdf', 'structured_test_pdf1.pdf') 
    input_json_path = os.path.join(base_dir, 'tests', 'test_files', 'json_files', 'summary_template.json')
    output_json_path = os.path.join(base_dir, 'tests', 'test_files', 'json_files', 'summary.json')

    summarize(pdf_path, output_pdf_path, input_json_path, output_json_path)
