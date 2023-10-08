import langchain_programming as lcp
import streamlit as lit
import os
lit.title("Morepain and Morepain")
user_documents = "user_documents"
prompt1 = lit.sidebar.selectbox("Please choose the best option that matches your selection.", ("Add/View Documents", "Document Summarization", "General Inquiry", "Interrogatory Summarization"))

if prompt1 == "Add/View Documents":
    semi_prompt1 = lit.sidebar.selectbox("Would you like to add or view a document?", ("Add", "View"))
    if semi_prompt1 == "Add":
        files = lit.file_uploader("Add Legal Documentation", type=["pdf"], accept_multiple_files=True, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
        # Check if the folder exists; if not, create it
        if not os.path.exists(user_documents):
            os.mkdir(user_documents)
        for file in files:
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
    


        
        