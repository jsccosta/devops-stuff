import re


def preprocess_page_1(text):
    """
    Preprocesses the text from page 1 by removing unwanted sections, 
    correcting line breaks and expanding abbreviations.

    Parameters:
    - text (str): The extracted text content from page 1.

    Returns:
    - str: The preprocessed text with corrections and expansions applied.
    """

    # Step 1: Remove the unwanted section starting from "1. 1.1" onwards
    text = re.sub(r'\s1\.\s1\.1.*$', '', text, flags=re.DOTALL)

    # Step 2: Remove newline between "100 MAIN ST" and "ANYWHERE"
    # Using regular expression to match and replace the pattern
    text = re.sub(r'100 MAIN\s*\n\s*ST ANYWHERE', '100 MAIN ST ANYWHERE', text)

    # Step 3: Expand specific phrases to complete sentences
    # Replace specific abbreviations and phrases with their expanded forms
    replacements = {
        'Risk Id:': 'The Risk Id is',
        '100 MAIN ST ANYWHERE': 'The location is 100 MAIN ST ANYWHERE',
        'Latest Update:': 'The last update was on',
        'On-Site Survey:': 'On-Site Survey took place on'
    }

    # Perform the replacements
    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def preprocess_page_2(text):
    """
    Preprocesses the text from page 2 by normalizing space characters
    and structuring key construction, occupancy and protection details.

    Parameters:
    - text (str): The extracted text content from page 2.

    Returns:
    - str: A newly structured summary emphasizing construction, 
    occupancy and protection details.
    """

    # Normalize the text by removing unwanted newlines and extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Construct a new preprocessed summary text
    preprocessed_text = "EXECUTIVE SUMMARY\n"

    # CONSTRUCTION section processing
    construction_match = re.search(
        r'CONSTRUCTION (.*?) ON-SITE VERIFIED: (\d{2}/\d{2}/\d{4}) (.*?) Building Square Footage: (\d+).*? Number of Stories: (\d+).*? Year Built: (\d+)',
        text, re.DOTALL)
    if construction_match:
        construction_details = f"- CONSTRUCTION:\n {construction_match.group(1)}"
        construction_details += f" The construction was ON-SITE VERIFIED on {construction_match.group(2)}."
        # Directly capturing the construction type detail following the verified date
        construction_details += f" The construction type is {construction_match.group(3)}."
        construction_details += f" The Building Square Footage is {construction_match.group(4)}."
        construction_details += f" The Number of Stories is {construction_match.group(5)}."
        construction_details += f" The Year Built is {construction_match.group(6)}.\n\n"
    else:
        construction_details = "- CONSTRUCTION:\n Details not found.\n\n"
    preprocessed_text += construction_details

    # OCCUPANCY section processing
    occupancy_pattern = re.compile(
        r'OCCUPANCY (.*?) (AUTOMATED VERIFIED: \d{2}/\d{2}/\d{4}).*?Primary Building Use (Restaurants|Resturants) (ISO CSP Class \d+ - [\w\s]+).*?Building Occupants ([\w\s]+) (ISO CSP Class \d+ - [\w\s]+)'
    )
    occupancy_match = occupancy_pattern.search(text)
    if occupancy_match:
        occupancy_details = "- OCCUPANCY:\n" + occupancy_match.group(1)
        occupancy_details += f" The occupancy was {occupancy_match.group(2)}."
        occupancy_details += f" The Primary Building Use is {occupancy_match.group(3)} {occupancy_match.group(4)}."
        occupancy_details += f" The Building Occupants are {occupancy_match.group(5)} {occupancy_match.group(6)}.\n\n"
    else:
        occupancy_details = "- OCCUPANCY:\nDetails not found.\n\n"
    preprocessed_text += occupancy_details

    # PROTECTION section processing
    protection_match = re.search(
        r'PROTECTION Sprinkler System: (N/A|[^.]+).*? Sprinkler Score: (N/A|[^.]+).*? ON-SITE VERIFIED: (\d{2}/\d{2}/\d{4}).*? Location Public Protection Classification: (\d+).*? VERIFIED: (\d{2}/\d{2}/\d{4})',
        text)
    if protection_match:
        sprinkler_system = "Not available" if protection_match.group(1) == "N/A" else protection_match.group(1)
        sprinkler_score = "Not available" if protection_match.group(2) == "N/A" else protection_match.group(2)
        protection_details = f"- PROTECTION:\n Sprinkler System is {sprinkler_system}. The Sprinkler Score is {sprinkler_score}. The protection was ON-SITE VERIFIED on {protection_match.group(3)}. The Location Public Protection Classification is {protection_match.group(4)}. It was VERIFIED on {protection_match.group(5)}.\n\n"
    else:
        protection_details = "- PROTECTION:\n Details not found.\n\n"
    preprocessed_text += protection_details

    return preprocessed_text


def preprocess_page_3(text):
    """
    Preprocesses the text from page 3 by normalizing text and 
    summarizing analytics and loss estimates.

    Parameters:
    - text (str): The extracted text content from page 3.

    Returns:
    - str: A newly structured summary of analytics and loss estimates.
    """

    # Normalize the text by removing unwanted newlines and extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Define patterns for extracting information
    analytics_pattern = re.compile(
        r'ANALYTICS RELATIVE HAZARD PERCENTILE (.*?) 0 Percentile')
    loss_estimates_pattern = re.compile(
        r'LOSS ESTIMATES Type I Loss (.*?) Risk Type I Loss Type II Loss Building: MAIN ST RESTAURANT (\d+)% (\d+)% Occupant: MAIN ST RESTAURANT (\d+)% (\d+)%')

    # Process ANALYTICS section
    analytics_match = analytics_pattern.search(text)
    analytics_text = "- RELATIVE HAZARD PERCENTILE:\n" + analytics_match.group(1) if analytics_match else "- RELATIVE HAZARD PERCENTILE:\nDetails not found."

    # Process LOSS ESTIMATES section
    loss_estimates_match = loss_estimates_pattern.search(text)
    if loss_estimates_match:
        loss_estimates_text = "- LOSS ESTIMATES:\nType I Loss is " + loss_estimates_match.group(1).replace('. ', '.')
        loss_estimates_text += "\nBased on the Risk:\n"
        loss_estimates_text += f"Type I Loss for Building MAIN ST RESTAURANT is {loss_estimates_match.group(2)}%\n"
        loss_estimates_text += f"Type II Loss for Building MAIN ST RESTAURANT is {loss_estimates_match.group(3)}%\n"
        loss_estimates_text += f"Type I Loss for Occupant MAIN ST RESTAURANT is {loss_estimates_match.group(4)}%\n"
        loss_estimates_text += f"Type II Loss for Occupant MAIN ST RESTAURANT is {loss_estimates_match.group(5)}%"
    else:
        loss_estimates_text = "- LOSS ESTIMATES:\nDetails not found."

    # Construct the final preprocessed summary text
    preprocessed_text = "ANALYTICS\n" + analytics_text + "\n\n" + loss_estimates_text

    return preprocessed_text


def preprocess_page_5(text):
    """
    Preprocesses text from page 5 to normalize content and 
    extract exposure information.

    Parameters:
    - text (str): The extracted text content from page 5.

    Returns:
    - str: A structured summary of exposure information.
    """

    # Normalize the text by removing unwanted newlines and extra spaces
    normalized_text = re.sub(r'\s+', ' ', text)

    # Define a pattern to extract the relevant pieces of information
    pattern = re.compile(
        r"Basic Group II Wind Symbol.*?Basic Group II (Exposure Information Location Wind - Detailed ®) "
        r"Distance to Ocean or Gulf: (\d+ miles to less than \d+ miles to Atlantic Ocean) "
        r"Distance to Nearest Body of Water: (\d+ mile to less than \d+ miles to Narragansett Bay) "
        r"Wind Geographic Risk Factor (Wind Geographic Risk Factor): (High)"
    )

    # Search for matches in the normalized text
    match = pattern.search(normalized_text)

    # Construct the formatted text if the pattern was matched
    if match:
        formatted_text = "Basic Group II\n- PROTECTION EXPOSURES\n"
        formatted_text += f"{match.group(1)}\n"
        formatted_text += f"Distance to Ocean or Gulf is {match.group(2)}\n"
        formatted_text += f"Distance to Nearest Body of Water is {match.group(3)}\n"
        formatted_text += f"{match.group(4)} is {match.group(5)}."
    else:
        formatted_text = "Details not found."

    return formatted_text


def preprocess_page_6(text):
    """
    Preprocesses text from page 6 to extract and summarize location details, 
    territory codes and crime information.

    Parameters:
    - text (str): The extracted text content from page 6.

    Returns:
    - str: A structured summary highlighting location details, 
    territory codes and crime information.
    """

    # Normalize the text by converting multiple spaces and newlines into single spaces
    text = re.sub(r'\s+', ' ', text)

    # Extract and format TERRITORY CODES
    territory_codes_pattern = r'ISO Commercial Territory Code: (\d+) ISO Group II Zone - Commercial: ([^.]+).*? ISO Commercial Auto Territory Code: (\d+)'
    territory_codes_match = re.search(territory_codes_pattern, text)
    territory_codes_text = "- TERRITORY CODES\n"
    if territory_codes_match:
        territory_codes_text += f"ISO Commercial Territory Code is {territory_codes_match.group(1)}\n"
        territory_codes_text += f"ISO Group II Zone Commercial is {territory_codes_match.group(2)}\n"
        territory_codes_text += f"ISO Commercial Auto Territory Code is {territory_codes_match.group(3)}\n\n"

    crime_info_pattern = re.compile(
        r'CRIME INFORMATION - COMMERCIAL LOCATION (CAP Index crime information.*?) Aggregate Crime Scores (Current Past Forecasted CAP Index.*?\.)')
    crime_info_match = crime_info_pattern.search(text)
    crime_info_text = "- CRIME INFORMATION - COMMERCIAL LOCATION\n" if crime_info_match else "- CRIME INFORMATION - COMMERCIAL LOCATION: Details not found.\n"
    if crime_info_match:
        crime_info_text += crime_info_match.group(1).strip() + "\n"

    # Dynamically extract Aggregate Crime Scores
    aggregate_scores_pattern = r'Aggregate Crime Scores(.+?)Individual Crime Scores'
    aggregate_scores_match = re.search(aggregate_scores_pattern, text, re.DOTALL)
    if aggregate_scores_match:
        aggregate_content = aggregate_scores_match.group(1).strip()
        # Dynamically parse the scores and their classifications
        scores = re.findall(r'(\d+) \((Class \d+)\)', aggregate_content)
        # Assuming a specific order: CAP Index, Crimes Against Person, Crimes Against Property
        score_titles = ["CAP Index", "Aggregate Crimes Against Person", "Aggregate Crimes Against Property"]
        crime_info_text += "Aggregate Crime Scores:\n"
        crime_info_text += f"{'Scores':60} {'Current':<10}      {'Past':<10}      {'Forecasted':<10}\n"
        for i, title in enumerate(score_titles):
            current, past, forecasted = scores[i*3:(i+1)*3]
            crime_info_text += f"{title:60} {' '.join(f'{score} ({cls})  ' for score, cls in [current, past, forecasted])}\n"
    else:
        crime_info_text += "Aggregate Crime Scores: Data not available.\n"

    preprocessed_text = "LOCATION DETAILS\n" + territory_codes_text + crime_info_text

    return preprocessed_text


def preprocess_page_7(text):
    """
    Preprocesses the text from page 7 to extract and 
    format specific business information.

    Parameters:
    - text (str): The extracted text content from page 7.

    Returns:
    - str: Formatted text highlighting key business information.
    """
        
    # Normalize the text by replacing multiple spaces and newlines with a single space for uniform processing
    normalized_text = re.sub(r'\s+', ' ', text)

    # Use a regex pattern to extract "Data provided by" information and "Number of Businesses at Address"
    pattern = re.compile(r'(BUSINESSES AT ADDRESS Data provided by \w+).*?Number of Businesses at Address:\s*(\d+)')
    match = pattern.search(normalized_text)

    if match:
        data_provider = match.group(1)  # Capture the "Data provided by" part dynamically
        num_businesses = match.group(2)  # Capture the number of businesses
        # Construct the preprocessed text using the dynamically captured information
        preprocessed_text = f"{data_provider}\n- Number of Businesses at Address is {num_businesses}"
    else:
        preprocessed_text = "Information not available"

    return preprocessed_text


def preprocess_page_8(text):
    """
    Preprocesses the text from page 8 to extract and 
    format detailed property, owner, sale, and tax information.

    Parameters:
    - text (str): The extracted text content from page 8.

    Returns:
    - str: Formatted text summarizing property characteristics,
    owner information, sale details and tax information.
    """
    # Normalize the text by converting multiple spaces to single spaces
    normalized_text = re.sub(r'\s+', ' ', text)

    # Define the structure of the sections and the corresponding regex patterns to extract the data
    sections = [
        ("PROPERTY CHARACTERISTICS", [
            ("Gross Area",  r"Gross Area: ([\d,]+)"),
            ("Condition",  r"Condition: (\w+)"),
        ]),
        ("OWNER INFORMATION", [
            ("Owner Name",  r"Mailing Address: ([\w\s]+?)\d"),
            ("Mailing Address",  r"Mailing Address: \D*(\d.+?) LAST MARKET SALE"),
        ]),
        ("LAST MARKET SALE INFORMATION", [
            ("Sale Date",  r"Recording - Sale Date: (\d{2}/\d{2}/\d{4})"),
            ("Sale Price",  r"Sale Price: ([\$\d,]+)"),
        ]),
        ("SITE INFORMATION", [
            ("Acres",  r"Acres: ([\d.]+)"),
            ("County",  r"County: (\w+)"),
            ("Lot Area",  r"Lot Area: ([\d,]+)"),
            ("Total Units",  r"Total Units: (\d+)"),
            ("# of Buildings",  r"# of Buildings: (\d+)"),
        ]),
        ("TAX INFORMATION", [
            ("Total Value",  r"Total Value: ([\$\d,]+)"),
            ("Land Value",  r"Land Value: ([\$\d,]+)"),
            ("Improvement Value",  r"Improvement Value: ([\$\d,]+)"),
            ("Market Value",  r"Market Value: (N/A|[\$\d,]+)"),
            ("Assessed Year",  r"Assessed Year: (\d+)"),
            ("Improve %",  r"Improve %: (\d+)%"),
        ])
    ]

    structured_text = ""
    for section_title, patterns in sections:
        structured_text += f"- {section_title}\n"
        for label, pattern in patterns:
            match = re.search(pattern, normalized_text)
            value = match.group(1).replace("N/A", "Not available") if match else "Not available"
            structured_text += f"  {label}: {value}\n"

    return structured_text.strip()