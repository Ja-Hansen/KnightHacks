import langchain_programming as lcp
import streamlit as lit
import os
from Summarize import summary
from langchain_programming import langchain_agent
from parce import parcer
from llama_index import (
    StorageContext,
    load_index_from_storage,
)
from llama_index.query_engine import RetrieverQueryEngine
import time
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
    #lit.subheader("Enter the pdf file name (without .pdf)")
    #pdf_title_ask = lit.text_input("pdf name")
    
    # Set environment variables
    os.environ["OPENAI_API_KEY"] = "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"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    # Number of chunks you would like to use for an answer.
    # Set to 1 to save money.
    k = 3

    # Rebuild storage context from the chunk storage
    storage_context = StorageContext.from_defaults(persist_dir="./chunkstorage")

    # Load index
    loadedIndex = load_index_from_storage(storage_context)

    # Create a Streamlit app
    lit.title("OpenAI Chatbot")

    timestamp = time.strftime("%Y_%m_%d-%H_%M_%S", time.gmtime())
    filename = "Llama" + timestamp + ".txt"

    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("User: Welcome to OpenAI chat!\n\n")

    user_input = lit.text_input("Enter your prompt:")
    if lit.button("Submit"):
        user_input = user_input.strip()
        if user_input == "":
            lit.warning("Please enter a prompt.")
        else:
            response = loadedIndex.as_retriever().query(user_input)

            lit.text("\nAI says:")
            lit.text(response)

            with open(filename, "a") as f:
                f.write("User:\n" + user_input + "\n\n")
                f.write("AI:\n" + str(response) + "\n\n")

    lit.text("Thanks for using our chatbot!")


        
            
            # Check if the folder exists; if not, create it
    
        
