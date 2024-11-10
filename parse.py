from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
    "Translate to English only"
)

model = OllamaLLM(model = "llama3.1")

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []
    
    # use 1-based index
    for i, chunk in enumerate(dom_chunks, start = 1):
        response = chain.invoke({"dom_content": chunk, "parse_description":parse_description})

        print(f"Parsed Batch {i} of {len(dom_chunks)}")
    
        parsed_results.append(response)

    return parsed_results


def combine_markdown_tables(result):
    """
    Parses a list of markdown table strings, converts them to DataFrames,
    and combines them into a single DataFrame.
    
    Parameters:
        result (list): A list of strings, where each string is a markdown table.
    
    Returns:
        pd.DataFrame: A combined DataFrame containing all rows from the tables.
    """
    all_dfs = []

    for response in result:
        rows = []
        for line in response.splitlines():
            if line.startswith("|") and not line.startswith("| ---"):
                rows.append([cell.strip() for cell in line.strip('|').split('|')])
        
        # Create DataFrame for the current table and add it to the list
        df = pd.DataFrame(rows[1:], columns=rows[0])  # Use the first row as headers
        all_dfs.append(df)

    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(all_dfs, ignore_index=True)
    
    return combined_df