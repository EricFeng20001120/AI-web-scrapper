import streamlit as st
from scrape import scrape_website, split_dom_content, clean_boady_content, extract_body_content
from parse import parse_with_ollama, combine_markdown_tables
import pandas as pd

"""
ctrl c to stop streamlit app
Please translate to English and extract job-related information from the HTML content, organizing it into a structured table with the following columns. Focus only on discussions about job roles, interview questions, online assessments (OA), team matches, and job-related experiences. For each relevant entry, include:

Category: Classify each entry into one of the following categories: Interview Question, OA, Experience, Package Detail, or other relevant job-related categories.
Job Title: The specific job title related to the discussion (e.g., "L3 SDE", "DS"). If the job title is not specified, fill with -.
Company: The name of the company associated with the job role or experience (e.g., "Google", "Amazon"). If the company is not specified, fill with -.
Topic: A brief, English title or summary (e.g., "Google Canada SRE Interview Questions"). Translate the title to English if necessary.
Content: A concise description in English, including details about the job role, interview questions, online assessments (OA), team match processes, or other relevant experiences. Translate any non-English text into English.
Link: For thread links in the format thread-xxxxxx-1-1.html, convert them to full URLs by adding https://www.1point3acres.com/bbs/ at the beginning (e.g., thread-1096746-1-1.html becomes https://www.1point3acres.com/bbs/thread-1096746-1-1.html).
Exclude unrelated content, navigation links, and general site features. Only extract entries that explicitly discuss roles, interviews, online assessments, hiring processes, or job-related experiences.

Output only the table with no other text.
SDE is software development engineer, DS is data scientist, MLE is machine learning engineer
"""


st.title("AI Web Scrapper")
url = st.text_input("Enter a RUL:")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)

    body_content = extract_body_content(result)
    clean_content = clean_boady_content(body_content)

    st.session_state.dom_content = clean_content

    # expander is a toggle when we press we can see DOM content
    with st.expander("View Dom content:"):
        st.text_area("DOM Content", clean_content, height=300)
    
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")
        
        dom_chunks = split_dom_content(st.session_state.dom_content)
        result = parse_with_ollama(dom_chunks,parse_description)

        #st.write(result)
        # print(result)
        # Convert markdown table to DataFrame
        combined_df = combine_markdown_tables(result)

        # Display DataFrame
        st.dataframe(combined_df)

        # Download DataFrame as CSV
        csv = combined_df.to_csv(index=False)
        st.download_button(
            label="Download as CSV",
            data=csv,
            file_name="parsed_results.csv",
            mime="text/csv"
        )