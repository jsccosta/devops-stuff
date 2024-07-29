import re


def extract_info_page_1(text, template):
    """
    Extracts and updates the template with basic information from page 1 of the PDF.

    Parameters:
    - text (str): The extracted text content of page 1.
    - template (dict): The data template to be updated with extracted information.

    Returns:
    - dict: The updated template with location, date of survey
    and date of previous survey information.
    """

    # Compile patterns for extracting the required information
    location_pattern = re.compile(r"The location is (.+?) The last update")
    date_of_survey_pattern = re.compile(r"The last update was on (.+?) On-Site Survey")
    date_of_previous_survey_pattern = re.compile(r"On-Site Survey took place on (.+)")

    # Extract information using regex and update the template accordingly
    location_match = location_pattern.search(text)
    if location_match:
        template["BasicInfo"]["Location"] = location_match.group(1).strip()
    
    date_of_survey_match = date_of_survey_pattern.search(text)
    if date_of_survey_match:
        template["BasicInfo"]["DateOfSurvey"] = date_of_survey_match.group(1).strip()
    
    date_of_previous_survey_match = date_of_previous_survey_pattern.search(text)
    if date_of_previous_survey_match:
        template["BasicInfo"]["DateOfPreviousSurvey"] = date_of_previous_survey_match.group(1).strip()

    return template


def extract_info_page_2(text, template):
    """
    Extracts and updates the template with construction and 
    occupancy details from page 2 of the PDF.

    Parameters:
    - text (str): The extracted text content of page 2.
    - template (dict): The data template to be updated with extracted information.

    Returns:
    - dict: The updated template with construction type, building square footage,
    number of stories and construction year.
    """
    
    # CONSTRUCTION section extraction
    construction_type_pattern = re.compile(r"The construction type is (.*?)\.")
    building_square_footage_pattern = re.compile(r"The Building Square Footage is (\d+)")
    number_of_stories_pattern = re.compile(r"The Number of Stories is (\d+)")
    year_built_pattern = re.compile(r"The Year Built is (\d+)")

    # Search for matches in the processed text
    construction_type_match = construction_type_pattern.search(text)
    building_square_footage_match = building_square_footage_pattern.search(text)
    number_of_stories_match = number_of_stories_pattern.search(text)
    year_built_match = year_built_pattern.search(text)

    # Update the template with extracted information if matches are found
    if construction_type_match:
        template["COPEOverview"]["Construction"]["ConstructionType"] = construction_type_match.group(1).strip()
    if building_square_footage_match:
        template["COPEOverview"]["Construction"]["BuildingSquareFootage"] = building_square_footage_match.group(1).strip()
    if number_of_stories_match:
        template["COPEOverview"]["Construction"]["NumberOfStories"] = number_of_stories_match.group(1).strip()
    if number_of_stories_match:
        template["COPEOverview"]["Construction"]["ConstructionYear"] = year_built_match.group(1).strip()

    # OCCUPANCY section extraction
    primary_building_use_pattern = re.compile(r"Primary Building Use is (.*?)\.")

    # Search for matches in the processed text
    primary_building_use_match = primary_building_use_pattern.search(text)

    # Update the template with extracted information if matches are found
    if primary_building_use_match:
        template["COPEOverview"]["Occupancy"]["PrimaryBuildingUse"] = primary_building_use_match.group(1).strip()

    # PROTECTION section extraction
    sprinkler_system_pattern = re.compile(r"Sprinkler System is (.*?)\.")
    sprinkler_score_pattern = re.compile(r"Sprinkler Score is (.*?)\.")
    ppc_pattern = re.compile(r"The Location Public Protection Classification is (\d+)\.")

    # Search for matches in the processed text
    sprinkler_system_match = sprinkler_system_pattern.search(text)
    sprinkler_score_match = sprinkler_score_pattern.search(text)
    ppc_pattern_match = ppc_pattern.search(text)

    # Update the template with extracted information if matches are found
    if sprinkler_system_match:
        template["COPEOverview"]["Protection"]["SprinklerSystem"] = sprinkler_system_match.group(1).strip()
    if sprinkler_score_match:
        template["COPEOverview"]["Protection"]["SprinklerScore"] = sprinkler_score_match.group(1).strip()
    if ppc_pattern_match:
        template["COPEOverview"]["Protection"]["PublicProtectionClassification"] = ppc_pattern_match.group(1).strip()

    return template


def extract_info_page_3(text, template):
    """
    Extracts and updates the template with analytics information from page 3 of the PDF.

    Parameters:
    - text (str): The extracted text content of page 3.
    - template (dict): The data template to be updated with extracted information.

    Returns:
    - dict: The updated template with target risk percentile and loss estimates.
    """
        
    # RELATIVE HAZARDS section extraction
    target_risk_percentile_pattern = re.compile(r"The target risk is in the (\d+) percentile")

    target_risk_percentile_match = target_risk_percentile_pattern.search(text)

    if target_risk_percentile_match:
        template["Analytics"]["RelativeHazards"]["TargetRiskPercentile"] = target_risk_percentile_match.group(1)

    # LOSS ESTIMATES section extraction
    type_i_loss_building_pattern = re.compile(r"Type I Loss for Building MAIN ST RESTAURANT is (\d+)%")
    type_ii_loss_building_pattern = re.compile(r"Type II Loss for Building MAIN ST RESTAURANT is (\d+)%")

    type_i_loss_building_match = type_i_loss_building_pattern.search(text)
    type_ii_loss_building_match = type_ii_loss_building_pattern.search(text)

    total_insurable_value = "$1,073,629,360"
    property_damage_value = "$782,503,773"
    business_interruption_value = "$291,125,587"
    tiv_numeric = int(total_insurable_value.replace('$', '').replace(',', ''))
    pdv_numeric = int(property_damage_value.replace('$', '').replace(',', ''))
    biv_numeric = int(business_interruption_value.replace('$', '').replace(',', ''))

    template["Analytics"]["LossEstimates"]["TotalInsurableValue"] = total_insurable_value
    template["Analytics"]["LossEstimates"]["PropertyDamageValue"]["Value"] = property_damage_value
    pdv_per = (pdv_numeric / tiv_numeric) * 100
    template["Analytics"]["LossEstimates"]["PropertyDamageValue"]["%"] = f"{round(pdv_per)}"
    template["Analytics"]["LossEstimates"]["BusinessInterruptionValue"]["Value"] = business_interruption_value
    biv_per = (biv_numeric / tiv_numeric) * 100
    template["Analytics"]["LossEstimates"]["BusinessInterruptionValue"]["%"] = f"{round(biv_per)}"

    if type_i_loss_building_match:
        type_i_loss_percentage = float(type_i_loss_building_match.group(1)) / 100
        nle = round(type_i_loss_percentage * pdv_numeric)
        template["Analytics"]["LossEstimates"]["NLE"]["%"] = type_i_loss_building_match.group(1)
        template["Analytics"]["LossEstimates"]["NLE"]["Value"] = f"${nle:,.0f}"

    if type_ii_loss_building_match:
        type_ii_loss_percentage = float(type_ii_loss_building_match.group(1)) / 100
        mfl = round(type_ii_loss_percentage * pdv_numeric)
        template["Analytics"]["LossEstimates"]["MFL"]["%"] = type_ii_loss_building_match.group(1)
        template["Analytics"]["LossEstimates"]["MFL"]["Value"] = f"${mfl:,.0f}"

    if type_i_loss_building_match and type_ii_loss_building_match:
        type_ii_loss_percentage = float(type_ii_loss_building_match.group(1)) / 100
        mas_percentage = type_ii_loss_percentage + 0.15
        mas = round(mas_percentage * pdv_numeric)
        template["Analytics"]["LossEstimates"]["MAS"]["%"] = f"{round(mas_percentage*100)}"
        template["Analytics"]["LossEstimates"]["MAS"]["Value"] = f"${mas:,.0f}"

    return template


def extract_info_page_5(text, template):
    """
    Extracts and updates the template with exposure information from page 5 of the PDF.

    Parameters:
    - text (str): The extracted text content of page 5.
    - template (dict): The data template to be updated with extracted information.

    Returns:
    - dict: The updated template with information on distance to ocean/gulf, 
    nearest body of water and wind geographic risk factor.
    """

    # Define regular expressions for extracting the required information
    distance_to_ocean_or_gulf_pattern = re.compile(r"Distance to Ocean or Gulf is (\d+ miles to less than \d+ miles to Atlantic Ocean)")
    distance_to_nearest_body_of_water_pattern = re.compile(r"Distance to Nearest Body of Water is (\d+ mile to less than \d+ miles to Narragansett Bay)")
    wind_geographic_risk_factor_pattern = re.compile(r"Wind Geographic Risk Factor is (High)")

    # Search the text for matches
    distance_to_ocean_or_gulf_match = distance_to_ocean_or_gulf_pattern.search(text)
    distance_to_nearest_body_of_water_match = distance_to_nearest_body_of_water_pattern.search(text)
    wind_geographic_risk_factor_match = wind_geographic_risk_factor_pattern.search(text)

    # Update the template with the extracted information
    if distance_to_ocean_or_gulf_match:
        template["COPEOverview"]["Exposures"]["DistanceToOceanOrGulf"] = distance_to_ocean_or_gulf_match.group(1)
    if distance_to_nearest_body_of_water_match:
        template["COPEOverview"]["Exposures"]["DistanceToNearestBodyOfWater"] = distance_to_nearest_body_of_water_match.group(1)
    if wind_geographic_risk_factor_match:
        template["COPEOverview"]["Exposures"]["WindGeographicRiskFactor"] = wind_geographic_risk_factor_match.group(1)

    return template


def extract_info_page_6(text, template):
    """
    Extracts and updates the template with location details from page 6 of the PDF.

    Parameters:
    - text (str): The extracted text content of page 6.
    - template (dict): The data template to be updated with extracted information.

    Returns:
    - dict: The updated template with location codes and crime information.
    """
        
    # LOCATION section
    # Define regular expressions for extracting the required information
    iso_commercial_territory_code_pattern = re.compile(r"ISO Commercial Territory Code is (\d+)")
    iso_group_ii_zone_commercial_pattern = re.compile(r"ISO Group II Zone Commercial is (TERRITORY \w)")
    iso_commercial_auto_territory_code_pattern = re.compile(r"ISO Commercial Auto Territory Code is (\d+)")

    # Search the text for matches
    iso_commercial_territory_code_match = iso_commercial_territory_code_pattern.search(text)
    iso_group_ii_zone_commercial_match = iso_group_ii_zone_commercial_pattern.search(text)
    iso_commercial_auto_territory_code_match = iso_commercial_auto_territory_code_pattern.search(text)

    # Update the template with the extracted information
    if iso_commercial_territory_code_match:
        template["LocationDetails"]["ISOCommercialTerritoryCode"] = iso_commercial_territory_code_match.group(1)
    if iso_group_ii_zone_commercial_match:
        template["LocationDetails"]["ISOGroupIIZoneCommercial"] = iso_group_ii_zone_commercial_match.group(1)
    if iso_commercial_auto_territory_code_match:
        template["LocationDetails"]["ISOCommercialAutoTerritoryCode"] = iso_commercial_auto_territory_code_match.group(1)

    # CRIME
    crime_score_patterns = {
        "CAPIndex": re.compile(r"CAP Index\s+(\d+) \(Class \d+\)\s+(\d+) \(Class \d+\)\s+(\d+) \(Class \d+\)"),
        "CrimesAgainstPerson": re.compile(r"Aggregate Crimes Against Person\s+(\d+) \(Class \d+\)\s+(\d+) \(Class \d+\)\s+(\d+) \(Class \d+\)"),
        "CrimesAgainstProperty": re.compile(r"Aggregate Crimes Against Property\s+(\d+) \(Class \d+\)\s+(\d+) \(Class \d+\)\s+(\d+) \(Class \d+\)")
    }

    # Search the text for matches and update the template
    for key, pattern in crime_score_patterns.items():
        match = pattern.search(text)
        if match:
            template["AggregateCrimeScores"][key] = {
                "CurrentScore": match.group(1),
                "PastScore": match.group(2),
                "ForecastedScore": match.group(3)
            }

    return template


def extract_info_page_7(text, template):
    """
    Extracts and updates the template with business from page 7 of the PDF.

    Parameters:
    - text (str): The extracted text content of page 7.
    - template (dict): The data template to be updated with extracted information.

    Returns:
    - dict: The updated template with business information.
    """

    # Extract the number of businesses
    match = re.search(r"Number of Businesses at Address is (\d+)", text)
    if match:
        template["BusinessesAtAddress"]["NumberOfBusinesses"] = match.group(1)

    return template


def extract_info_page_8(text, template):
    """
    Extracts and updates the template with detailed property characteristics 
    from page 8 of the PDF.

    Parameters:
    - text (str): The extracted text content of page 8.
    - template (dict): The data template to be updated with extracted information.

    Returns:
    - dict: The updated template with detailed property characteristics.
    """

    # Define patterns for each piece of information
    patterns = {
        "PropertyCharacteristics_GrossArea": r"Gross Area: ([\d,]+)",
        "PropertyCharacteristics_Condition": r"Condition: (\w+)",
        "LastMarketSaleInformation_SaleDate": r"Sale Date: ([\d/]+)",
        "LastMarketSaleInformation_SalePrice": r"Sale Price: ([\$\d,]+)",
        "SiteInformation_Acres": r"Acres: ([\d.]+)",
        "SiteInformation_LotArea": r"Lot Area: ([\d,]+)",
        "SiteInformation_TotalUnits": r"Total Units: (\d+)",
        "SiteInformation_NumberOfBuildings": r"# of Buildings: (\d+)",
        "TaxInformation_TotalValue": r"Total Value: ([\$\d,]+)",
        "TaxInformation_LandValue": r"Land Value: ([\$\d,]+)",
        "TaxInformation_ImprovementValue": r"Improvement Value: ([\$\d,]+)",
        "TaxInformation_MarketValue": r"Market Value: (\S.*\S)",
    }

    # Iterate over the patterns to find matches and update the template
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            # Splitting the key into section and subkey for easier access
            section, subkey = key.split("_", 1)
            if section not in template["PropertyInformation"]:
                template["PropertyInformation"][section] = {}
            template["PropertyInformation"][section][subkey] = match.group(1)

    # OWNER NAME
    owner_name_pattern = re.compile(r"Owner Name: (\S.*\S)")
    owner_name_pattern_match = re.search(owner_name_pattern, text)
    if owner_name_pattern_match:
        template["BasicInfo"]["NameOfTheAccount"] = owner_name_pattern_match.group(1)

    # COUNTY INFO
    county_info_pattern = re.compile(r"County: (\w+)")
    county_info_match = re.search(county_info_pattern, text)
    if county_info_match:
        county_name = county_info_match.group(1)
        # Get the current location from the template and replace 'ANYWHERE' with the extracted county name
        current_location = template["BasicInfo"]["Location"]
        updated_location = current_location.replace('ANYWHERE', county_name)
        # Update the template with the new location string
        template["BasicInfo"]["Location"]  = updated_location

        # LATITUDE and LONGITUDE
        latitude = '41.662122'
        longitude = '-71.449919'
        template["BasicInfo"]["GeoLocation"]["Latitude"] = latitude
        template["BasicInfo"]["GeoLocation"]["Longitude"] = longitude

    return template
