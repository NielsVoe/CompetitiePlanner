# save as app.py
import streamlit as st
import CompetitiePlanner as CP

st.title("Simple Web Scraper and Data Editor")

# URL input
url = st.text_input("Enter a URL to scrape", "https://example.com")

if st.button("Scrape"):
    print("Scraping data from:", url)
    CP.main()
