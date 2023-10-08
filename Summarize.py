import openai 
import PyPDF2
import re
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')
pdf_summary_text = ""
pdf_file_path = input("Enter pdf file name (without .pdf): ") + ".pdf"
pdf_file = open(pdf_file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
for page_num in range(len(pdf_reader.pages)):
    page_text = pdf_reader.pages[page_num].extract_text().lower()
    response = openai.ChatCompletion.create(
            model = "gpt-4",
            messages = [
                {"role": "system", "content": "You are a helpful research assistant."},
                {"role": "user", "content": f"Summarize this very concisely: {page_text}"},
                    ],
                        )
    page_summary = response["choices"][0]["message"]["content"]
    pdf_summary_text += page_summary + "\n"

pdf_summary_file = pdf_file_path.replace(os.path.splitext(pdf_file_path)[1], "_summary.txt")

# Write the summary to the file
with open(pdf_summary_file, 'w') as summary_file:
    summary_file.write(pdf_summary_text)

print(f"Summary made. Saved to: {pdf_summary_file}")
