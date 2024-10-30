import streamlit as st
from scrape import scrape_website, split_dom_content, clean_boady_content, extract_body_content
from parse import parse_with_ollama
"""
ctrl c to stop streamlit app
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

        st.write(result)