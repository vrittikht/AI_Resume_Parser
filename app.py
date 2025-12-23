import os
import platform
import subprocess
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from parser import extract_text
from utils import extract_entities_with_model, clean_illegal_chars

OUTPUT_FILE = "output/parsed_resumes.xlsx"

def upload_files():
    file_paths = filedialog.askopenfilenames(
        title="Select Resume Files",
        filetypes=[("Resume Files", "*.pdf *.docx *.doc *.png *.jpg *.jpeg")]
    )

    if not file_paths:
        return

    parsed_results = []

    for file_path in file_paths:
        try:
            absolute_path = os.path.abspath(file_path)
            text = extract_text(absolute_path)
            extracted = extract_entities_with_model(text)
            cleaned = {k: clean_illegal_chars(v) for k, v in extracted.items()}
            parsed_results.append(cleaned)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process:\n{file_path}\n\nReason:\n{str(e)}")

    if parsed_results:
        new_df = pd.DataFrame(parsed_results)

        # Append to existing Excel file if exists
        if os.path.exists(OUTPUT_FILE):
            existing_df = pd.read_excel(OUTPUT_FILE)
            final_df = pd.concat([existing_df, new_df], ignore_index=True)
        else:
            final_df = new_df

        final_df.to_excel(OUTPUT_FILE, index=False)



        # Path to your output Excel file
        output_path = os.path.abspath("output/parsed_resumes.xlsx")

        # Open the file (cross-platform support)
        if platform.system() == "Windows":
            os.startfile(output_path)
        elif platform.system() == "Darwin":  # macOS
            subprocess.call(["open", output_path])
        else:  # Linux
            subprocess.call(["xdg-open", output_path])

        messagebox.showinfo("Success", f"{len(parsed_results)} resume(s) processed and saved!")
    else:
        messagebox.showwarning("No Data", "No resumes were successfully processed.")

def build_gui():
    window = tk.Tk()
    window.title("Resume Parser AI")
    window.geometry("400x200")
    window.resizable(False, False)

    label = tk.Label(window, text="Upload Resume Files", font=("Segoe UI", 14))
    label.pack(pady=30)

    upload_btn = tk.Button(window, text="Browse Resumes", command=upload_files, font=("Segoe UI", 12), width=20)
    upload_btn.pack()

    window.mainloop()

if __name__ == "__main__":
    build_gui()
