# save as app.py
import streamlit as st
import CompetitiePlanner as CP
from src.Club import Club
from src.Gender import Gender

st.title("Competitie Planner BC Geldrop")

mainPage = st.Page("pages/mainPage.py", title="Uitleg")
teamPage = st.Page("pages/teamPage.py", title="Teams")

pg = st.navigation([mainPage, teamPage])

pg.run()

# URL input

if st.button("Scrape"):
    st.write("Scraping data from:", CP.GetUrl())
    try:
        CP.RetrieveData()
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    
    club:Club = CP.GetClub()
    for team in club.GetTeams():
        st.write(f"Team: {team.name}")
        st.write(f"  Heren:")
        for player in team.players:
            if player.gender == Gender.MALE:
                st.write(player.name)
        st.write(f"  Dames:")
        for player in team.players:
            if player.gender == Gender.FEMALE:
                st.write(player.name)

    
