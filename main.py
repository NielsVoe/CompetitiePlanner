# save as app.py
import streamlit as st
import CompetitiePlanner as CP
from src.Club import Club
from src.Gender import Gender

st.title("Simple Web Scraper and Data Editor")

# URL input
url = st.text_input("Enter a URL to scrape", "https://example.com")

if st.button("Scrape"):
    st.write("Scraping data from:", url)
    # try:
    #     CP.RetrieveData()
    #     st.success("Data scraped successfully!")
    # except Exception as e:
    #     st.error(f"An unexpected error occurred: {e}")
    
    # club:Club = CP.GetClub()
    # for team in club.teams:
    #     st.write(f"Team: {team.name}")
    #     st.write(f"  Heren:")
    #     for player in team.players:
    #         if player.gender == Gender.MALE:
    #             st.write(player.name)
    #     st.write(f"  Dames:")
    #     for player in team.players:
    #         if player.gender == Gender.FEMALE:
    #             st.write(player.name)

    
