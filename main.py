# save as app.py
import streamlit as st
from pages.teamPage import TeamPage
import pages.mainPage as mainPage

st.title("Competitie Planner BC Geldrop")

homePage = st.Page("pages/mainPage.py", title="Uitleg")
numberOfTeams = mainPage.GetNumberOfTeams()

teamPages = []

for i in range(1, numberOfTeams + 1):
    team = TeamPage(mainPage.GetClub(), teamName=f"Team {i}")
    teamPages.append((team.DisplayTeam(), f"Team {i}"))

pg = st.navigation(teamPages)

pg.run()
