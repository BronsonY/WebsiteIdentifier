import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_TOKEN"),
            model_name="llama-3.1-70b-versatile"
        )
        self.max_chars = 2000  # Adjust based on token requirements

    def extract_jobs(self, cleaned_text):
        # Split input into manageable chunks
        chunks = [cleaned_text[i:i+self.max_chars] for i in range(0, len(cleaned_text), self.max_chars)]
        all_results = []

        for chunk in chunks:
            prompt_extract = PromptTemplate.from_template(
                """
                ### SCRAPED TEXT FROM WEBSITE:
                {page_data}
                ### INSTRUCTION:
                The scraped text is from the page of a website.
                What is this site about? Summarize in one sentence or paragraph.
                ### (NO PREAMBLE):
                """
            )
            chain_extract = prompt_extract | self.llm

            try:
                res = chain_extract.invoke(input={"page_data": chunk})
                all_results.append(res.content.strip())
            except Exception as e:
                raise Exception(f"Error processing chunk: {e}")

        # Combine results into one paragraph
        return " ".join(all_results)

if __name__ == "__main__":
    print(os.getenv("GROQ_API_TOKEN"))
