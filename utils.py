import spacy
import re

# Load the custom trained NER model
nlp = spacy.load("resume_parser_training/output_model")

def extract_entities_with_model(text):
    doc = nlp(text)
    result = {
        "Name": "",
        "Contact": "",
        "Email ID": "",
        "Highest Qualification with Year": "",
        "Current Company": "",
        "Department": "",
        "Current Designation": "",
        "Total Experience": "",
        "Current Location": "",
        "Native Place": ""
    }

    for ent in doc.ents:
        label = ent.label_.upper()
        value = ent.text.strip()

        if label == "NAME" and not result["Name"]:
            result["Name"] = value
        elif label == "PHONE" and not result["Contact"]:
            result["Contact"] = value
        elif label == "EMAIL" and not result["Email ID"]:
            result["Email ID"] = value
        elif label == "QUALIFICATION" and not result["Highest Qualification with Year"]:
            result["Highest Qualification with Year"] = value
        elif label == "COMPANY" and not result["Current Company"]:
            result["Current Company"] = value
        elif label == "DEPARTMENT" and not result["Department"]:
            result["Department"] = value
        elif label == "DESIGNATION" and not result["Current Designation"]:
            result["Current Designation"] = value
        elif label == "EXPERIENCE" and not result["Total Experience"]:
            result["Total Experience"] = value
        elif label == "CURRENT_LOCATION" and not result["Current Location"]:
            result["Current Location"] = value
        elif label == "NATIVE_PLACE" and not result["Native Place"]:
            result["Native Place"] = value

    return result

def clean_illegal_chars(text):
    # Clean Excel-invalid characters
    return re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text).strip()
