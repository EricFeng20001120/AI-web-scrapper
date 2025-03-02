# AI Web Scraper with Streamlit, Python, and Ollama

## Overview
This project is an **AI-powered web scraper** that extracts and parses web content using **Streamlit, Selenium, BeautifulSoup, and Ollama**. Users can input a URL, scrape the webpage, view the cleaned DOM content, and extract specific information using AI-powered parsing.
The detail tutorial can be found in https://medium.com/@yixin.feng20001120/building-an-ai-powered-web-scraper-with-streamlit-python-and-ollama-c8f79041c634

## Features
- **Web Scraping:** Uses Selenium to fetch webpage content.
- **Content Cleaning:** BeautifulSoup removes scripts, styles, and unnecessary elements.
- **AI-Powered Parsing:** Ollama extracts relevant information based on user-defined queries.
- **Streamlit UI:** Interactive interface for ease of use.

## Tech Stack
- **Python 3.8+**
- **Streamlit** (UI framework)
- **Selenium & BeautifulSoup** (Web scraping)
- **Ollama** (AI parsing)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/EricFeng20001120/AI-web-scrapper.git
cd ai-web-scraper
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App
```bash
streamlit run main.py
```

Press **Ctrl+C** to stop the app.

## Usage
1. Enter a **URL** in the text input field.
2. Click **"Scrape Site"** to extract the webpage's content.
3. View the cleaned **DOM content** in an expander.
4. Describe what you want to extract in the text area.
5. Click **"Parse Content"** to extract relevant information using AI.

## Project Structure
```
📂 ai-web-scraper
├── 📜 main.py            # Streamlit UI
├── 📜 scrape.py          # Web scraping functions
├── 📜 parse.py           # AI parsing with Ollama
├── 📜 requirements.txt   # Dependencies
└── 📜 README.md          # Project documentation
```

## Dependencies
Ensure the following dependencies are installed:
```bash
streamlit
selenium
webdriver-manager
beautifulsoup4
langchain_ollama
```

## Contributing
Feel free to open issues or submit pull requests if you have improvements or feature suggestions!

## License
MIT License

---

### 🚀 Happy Scraping!

