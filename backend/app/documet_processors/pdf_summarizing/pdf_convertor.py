from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
import json


def load_json_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)
    

def generate_pdf(json_data, output_filepath):
    # Reduced margins
    doc = SimpleDocTemplate(output_filepath, pagesize=letter, 
                            leftMargin=46, rightMargin=46, 
                            topMargin=36, bottomMargin=36)  # Margins in points (1 inch = 72 points) 
    story = []
    styles = getSampleStyleSheet()

    # Add document title
    title = "RISK MANAGEMENT REPORT SUMMARY"
    story.append(Paragraph(title, styles['Title']))
    story.append(Spacer(1, 20))  # Add some space after the title


    def add_section(title, data, style=None):
        story.append(Paragraph(title, styles['Heading3']))
        #story.append(Paragraph(title, styles['SectionTitle']))
        for key, value in data:
            if style == 'table':
                table_style = TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ])
                t = Table(value, style=table_style)
                story.append(t)
            else:
                paragraph = Paragraph(f"<b>{key}:</b> {value}", styles['BodyText'])
                # paragraph_text = f"{key}: {value}"
                # paragraph = Paragraph(paragraph_text, styles['KeyStyle'])
            story.append(paragraph)
        story.append(Spacer(1, 12))

    # Reusing the existing add_section helper function for uniformity

    # Basic Information section (existing code)
    basic_info_contents = [
        ("Name of the Account", json_data["BasicInfo"]["NameOfTheAccount"]),
        ("Location", json_data["BasicInfo"]["Location"]),
        ("Latitude", json_data["BasicInfo"]["GeoLocation"]["Latitude"]),
        ("Longitude", json_data["BasicInfo"]["GeoLocation"]["Longitude"]),
        ("Date of the Survey", json_data["BasicInfo"]["DateOfSurvey"]),
        ("Date of the Previous Survey", json_data["BasicInfo"]["DateOfPreviousSurvey"])
    ]
    add_section("BASIC INFORMATION", basic_info_contents)

    # COPE Overview section
    cope_contents = [
        ("Construction Type", json_data["COPEOverview"]["Construction"]["ConstructionType"]),
        ("Building Square Footage", json_data["COPEOverview"]["Construction"]["BuildingSquareFootage"]),
        ("Number of Stories", json_data["COPEOverview"]["Construction"]["NumberOfStories"]),
        ("Construction Year", json_data["COPEOverview"]["Construction"]["ConstructionYear"]),
        ("Primary Building Use", json_data["COPEOverview"]["Occupancy"]["PrimaryBuildingUse"]),
        ("Sprinkler System", json_data["COPEOverview"]["Protection"]["SprinklerSystem"]),
        ("Sprinkler Score", json_data["COPEOverview"]["Protection"]["SprinklerScore"]),
        ("Public Protection Classification", json_data["COPEOverview"]["Protection"]["PublicProtectionClassification"]),
        ("Distance to Ocean or Gulf", json_data["COPEOverview"]["Exposures"]["DistanceToOceanOrGulf"]),
        ("Distance to Nearest Body of Water", json_data["COPEOverview"]["Exposures"]["DistanceToNearestBodyOfWater"]),
        ("Wind Geographic Risk Factor", json_data["COPEOverview"]["Exposures"]["WindGeographicRiskFactor"])
    ]
    add_section("COPE OVERVIEW", cope_contents)

    # Analytics Section with Relative Hazards displayed normally
    analytics_relative_hazards_content = [
        ("Target Risk Percentile", json_data["Analytics"]["RelativeHazards"]["TargetRiskPercentile"])
    ]
    add_section("RELATIVE HAZARDS", analytics_relative_hazards_content)

    def add_loss_estimates_section(title, json_data):
        story.append(Paragraph(title, styles['Heading3']))
        # Define the table header without extra spaces, as alignment and color will be handled via TableStyle
        data = [["Loss Estimates", "%", "Value"]]
    
        # Define loss types to include in the table
        loss_types = [
            ("Property Damage Value", "PropertyDamageValue"),
            ("Business Interruption Value", "BusinessInterruptionValue"),
            ("PD MAS", "MAS"),
            ("PD MFL", "MFL"),
            ("PD NLE", "NLE")
        ]
    
        # Append each loss type with its percentage and value
        for label, key in loss_types:
            percent = json_data["Analytics"]["LossEstimates"][key]["%"]
            value = json_data["Analytics"]["LossEstimates"][key]["Value"]
            data.append([label, percent, value])

        # Create the table with the data, adjusting colWidths and alignment as needed
        table = Table(data, colWidths=[150, 50, 100], hAlign='LEFT')
        table.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,0), (2,0), colors.grey),  # Apply grey background to header row
            ('TEXTCOLOR', (0,0), (2,0), colors.whitesmoke),  # White text color for header row
            #('ALIGN', (0,0), (2,0), 'CENTER'),  # Center align header cells
            ('ALIGN', (0,1), (-1,-1), 'LEFT'),  # Left align non-header cells
            ('FONTNAME', (0,0), (2,0), 'Helvetica-Bold'),  # Bold font for header row
            ('BACKGROUND', (0,1), (-1,-1), colors.white),  # Apply white background to the rest of the table
        ]))
    
        story.append(table)
        story.append(Spacer(1, 12))


    add_loss_estimates_section("LOSS ESTIMATES", json_data)

    # Location Details section
    location_details_contents = [
        ("ISO Commercial Territory Code", json_data["LocationDetails"]["ISOCommercialTerritoryCode"]),
        ("ISO Group II Zone Commercial", json_data["LocationDetails"]["ISOGroupIIZoneCommercial"]),
        ("ISO Commercial Auto Territory Code", json_data["LocationDetails"]["ISOCommercialAutoTerritoryCode"])
    ]
    add_section("LOCATION DETAILS", location_details_contents)

    def add_aggregate_crime_scores_section(title, json_data):
        story.append(Paragraph(title, styles['Heading3']))
        # Define the table header
        data = [["", "Current Score", "Past Score", "Forecasted Score"]]
        # Append each category of crimes with its scores
        categories = ["CAP Index", "Crimes Against Person", "Crimes Against Property"]
        for category in categories:
            row = [category]
            for score_type in ["CurrentScore", "PastScore", "ForecastedScore"]:
                key = f"{category.replace(' ', '')}_{score_type}"
                row.append(json_data["AggregateCrimeScores"][category.replace(' ', '')][score_type])
            data.append(row)
        
        # Create the table with the data
        table = Table(data, colWidths=[120, 90, 90, 90], hAlign='LEFT')
        table.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (1,1), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ]))
        story.append(table)
        story.append(Spacer(1, 12))

    add_aggregate_crime_scores_section("Aggregated Crime Scores", json_data)

    # Businesses At Address section
    businesses_contents = [
        ("Number of Businesses", json_data["BusinessesAtAddress"]["NumberOfBusinesses"])
    ]
    add_section("BUSINESSES AT ADDRESS", businesses_contents)

    # Property Information section
    property_info_contents = [
        ("Gross Area", json_data["PropertyInformation"]["PropertyCharacteristics"]["GrossArea"]),
        ("Condition", json_data["PropertyInformation"]["PropertyCharacteristics"]["Condition"]),
        ("Sale Date", json_data["PropertyInformation"]["LastMarketSaleInformation"]["SaleDate"]),
        ("Sale Price", json_data["PropertyInformation"]["LastMarketSaleInformation"]["SalePrice"]),
        ("Acres", json_data["PropertyInformation"]["SiteInformation"]["Acres"]),
        ("Lot Area", json_data["PropertyInformation"]["SiteInformation"]["LotArea"]),
        ("Total Units", json_data["PropertyInformation"]["SiteInformation"]["TotalUnits"]),
        ("Number of Buildings", json_data["PropertyInformation"]["SiteInformation"]["NumberOfBuildings"]),
        ("Total Value", json_data["PropertyInformation"]["TaxInformation"]["TotalValue"]),
        ("Land Value", json_data["PropertyInformation"]["TaxInformation"]["LandValue"]),
        ("Improvement Value", json_data["PropertyInformation"]["TaxInformation"]["ImprovementValue"]),
        ("Market Value", json_data["PropertyInformation"]["TaxInformation"]["MarketValue"])
    ]
    add_section("PROPERTY INFORMATION", property_info_contents)

    recommendation_contents = [
        ("Date of Recommendation", json_data['Recommendation']["DateOfRecommendation"]),
        ("Ranking", json_data['Recommendation']["Ranking"]),
        ("Type", json_data['Recommendation']["Type"]),
        ("Details of Recommendation", json_data['Recommendation']["DetailsOfRecommendation"]),
        ("Impact on Loss Estimates", json_data['Recommendation']["ImpactOnLossEstimates"]),
        ("Status", json_data['Recommendation']["Status"]),
        ("Client Comments", json_data['Recommendation']["ClientComments"]),
    ]

    add_section("RECOMMENDATION", recommendation_contents)
    

    # Building the document
    doc.build(story)


def main():
    json_data = load_json_data("updated_risk_management_summary.json")
    generate_pdf(json_data, "output3.pdf")

if __name__ == "__main__":
    main()