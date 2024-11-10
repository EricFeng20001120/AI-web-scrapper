import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


import time

def scrape_website(website):
    print("Launching chorme browser...")

    #chrome_driver_path = "./chrome-win64/chrome.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content,"html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_boady_content(body_content):
    # soup will be HTML content, can access elements by tag
    soup = BeautifulSoup(body_content, "html.parser")
    
    # remove script and style
    for script_or_style in soup(['script','style']):
        script_or_style.extract()

    # Extract table content
    tables = []
    for table in soup.find_all('table'):
        table_data = []
        for row in table.find_all('tr'):
            row_data = []
            for cell in row.find_all(['td', 'th']):  # Capture both headers and regular cells
                text = cell.get_text(strip=True)
                link = cell.find('a')
                link = link.get('href') if link else None
                if link:
                    row_data.append(f"{text} (Link: {link})")
                else:
                    row_data.append(text)
            if row_data:
                table_data.append(row_data)
        if table_data:
            tables.append(table_data)

    # Join all tables as strings for easier handling
    tables_str = "\n\n".join(
        ["\n".join(["\t".join(row) for row in table]) for table in tables]
    )

    return tables_str

def clean_boady_content_only_str(body_content):
    # soup will be HTML content, can access elements by tag
    soup = BeautifulSoup(body_content, "html.parser")
    
    # remove script and style
    for script_or_style in soup(['script','style']):
        script_or_style.extract()

    clean_content = soup.get_text(separator = "\n")
    clean_content = "\n".join(
        line.strip() for line in clean_content.splitlines() if line.strip()
    )

    return clean_content

def split_dom_content(dom_content, max_length = 6000):
    # split into document with length = max_length
    return [
        dom_content[i:i+max_length] for i in range(0,len(dom_content), max_length)
    ]
