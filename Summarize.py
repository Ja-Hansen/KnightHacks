import openai 
import PyPDF2
# import re
import os

# Set the OpenAI API key from the environment variable 'OPENAI_API_KEY'
# The user needs to use their key stored on their computer.
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Initialize an empty string to store the summarized text of the PDF
pdf_summary_text = ""

pdf_file_path = input("Enter pdf file name (without .pdf): ") + ".pdf"

# Open the specified PDF file in binary read mode
pdf_file = open(pdf_file_path, 'rb')

# Use PyPDF2 to read the content of the opened PDF file
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Iterate over each page in the PDF
for page_num in range(len(pdf_reader.pages)):
    # Extract the text from the current page and convert it to lowercase
    page_text = pdf_reader.pages[page_num].extract_text().lower()
    
    # Make a request to OpenAI's ChatCompletion API to summarize the extracted text
    # The model "gpt-4" is used, and a system message sets the role of the model as a research assistant
    response = openai.ChatCompletion.create(
            model = "gpt-4",
            messages = [
                {"role": "system", "content": "You are a helpful research assistant."},
                {"role": "user", "content": f"Summarize this very concisely: {page_text}"},
                    ],
                        )
    
    # Extract the summarized content from the API response
    page_summary = response["choices"][0]["message"]["content"]
    
    # Append the summarized content to the overall summary text
    pdf_summary_text += page_summary + "\n"

# Create a new file path for the summary by replacing the ".pdf" extension with "_summary.txt"
pdf_summary_file = pdf_file_path.replace(os.path.splitext(pdf_file_path)[1], "_summary.txt")

# Write the overall summarized text to the new summary file
with open(pdf_summary_file, 'w') as summary_file:
    summary_file.write(pdf_summary_text)

# Print the location where the summary file has been saved
print(f"Summary made. Saved to: {pdf_summary_file}")

