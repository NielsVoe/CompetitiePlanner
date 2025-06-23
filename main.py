# save as app.py
import streamlit as st
import CompetitiePlanner as CP
from src.Club import Club
from src.Gender import Gender

st.title("Simple Web Scraper and Data Editor")

# URL input

if st.button("Scrape"):
    print("Scraping data from:", CP.GetUrl())
    try:
        CP.RetrieveData()
        st.success("Data scraped successfully!")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    
    club:Club = CP.GetClub()
    for team in club.GetTeams():
        print(f"Team: {team.name}")
        print(f"  Heren:")
        for player in team.players:
            if player.gender == Gender.MALE:
                print(player.name)
        print(f"  Dames:")
        for player in team.players:
            if player.gender == Gender.FEMALE:
                print(player.name)

    
