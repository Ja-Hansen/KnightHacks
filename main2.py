import langchain_programming as lcp
import streamlit as lit

lit.title("Morepain and Morepain")

prompt1 = lit.sidebar.selectbox("Please choose the best option that matches your selection.", ("Add/View Documents", "Document Summarization", "General Inquriry", "Interrogatory Summarization"))

if prompt1 == "Add/View Documents":
    
