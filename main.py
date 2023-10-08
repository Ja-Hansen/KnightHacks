import langchain_programming as lcp
import streamlit as lit
import os
from Summarize import summary
from langchain_programming import langchain_agent


lit.title("Morepain and Morepain")
user_documents = "user_documents"
prompt1 = lit.sidebar.selectbox("Please choose the best option that matches your selection.", ("Add/View Documents", "Document Summarization", "General Inquiries", "Ask about Document"))

if prompt1 == "Add/View Documents":
    semi_prompt1 = lit.sidebar.selectbox("Would you like to add or view a document?", ("Add", "View"))
    if semi_prompt1 == "Add":
        add_files = lit.file_uploader("Add Legal Documentation", type=["pdf"], accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
        # Check if the folder exists; if not, create it
        if not os.path.exists(user_documents):
            os.mkdir(user_documents)
        for file in add_files:
            # Save the file to the "user_documents" folder
            file_path = os.path.join(user_documents, file.name)
            with open(file_path, "wb") as f:
                f.write(file.read())
            lit.write("Filename:", file.name)
            lit.write("File has been accepted!")
    else:
        lit.subheader("PDF Documents currently submitted.")
        # Get a list of PDF files in the user_documents folder
        pdf_files = [f for f in os.listdir(user_documents) if f.endswith(".pdf")]

        # Display the titles of PDF documents as clickable links
        for pdf_file in pdf_files:
            # Create a clickable link to open the PDF using HTML
            pdf_link = f'<a href="{os.path.join(user_documents, pdf_file)}" target="_blank">{pdf_file}</a>'
            lit.markdown(pdf_link, unsafe_allow_html=True)

if prompt1 == "Document Summarization":
    lit.subheader("Enter pdf file name (without .pdf)")
    pdf_title_sum = lit.text_input("pdf name")
    summary_result = summary(pdf_title_sum)
    lit.markdown(body = summary_result)

if prompt1 == "General Inquiries":
    lit.subheader("Enter any questions related to Morgan&Morgan, the law, or any court proceesings. Our chat bot will try our best to explain it to you :)")
    inquiry = lit.text_input("Enter question below")
    inquiry_result = langchain_agent(inquiry)
    lit.markdown(body = inquiry_result)

if prompt1 == "Ask about Document":
    lit.subheader("This is an upcoming feature.") ## data parsing is working on terminal only at the moment