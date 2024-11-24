import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from utils import clean_text

def create_streamlit_app(llm, clean_text_func):
    st.title("📧 Get Information About a Website")
    url_input = st.text_input("Enter a URL:", value="")
    submit_button = st.button("Submit")

    if submit_button:
        if not url_input.strip():
            st.error("Please enter a valid URL.")
            return

        try:
            loader = WebBaseLoader([url_input])
            data = clean_text_func(loader.load().pop().page_content)
            result = llm.extract_jobs(data)

            st.success("Extracted Information:")
            st.write(result)  # Display result as plain text in Streamlit

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    st.set_page_config(
        layout="wide", 
        page_title="Get Information About a Website", 
        page_icon="📧"
    )
    create_streamlit_app(chain, clean_text)
