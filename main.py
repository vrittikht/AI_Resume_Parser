# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from utils import extract_entities_with_model, clean_illegal_chars
from parser import extract_text
import os
import pandas as pd

RESUME_FOLDER = "resumes"
OUTPUT_FILE = "output/parsed_resumes.xlsx"

parsed_data = []

for filename in os.listdir(RESUME_FOLDER):
    file_path = os.path.join(RESUME_FOLDER, filename)
    if os.path.isfile(file_path):
        print(f"📄 Parsing: {filename}")
        text = extract_text(file_path)
        extracted = extract_entities_with_model(text)
        cleaned = {key: clean_illegal_chars(val) for key, val in extracted.items()}
        parsed_data.append(cleaned)

df = pd.DataFrame(parsed_data)

# Save to Excel without overwriting previous data
if os.path.exists(OUTPUT_FILE):
    existing_df = pd.read_excel(OUTPUT_FILE)
    df = pd.concat([existing_df, df], ignore_index=True)

df.to_excel(OUTPUT_FILE, index=False)
print("✅ Parsing completed and saved to Excel.")
