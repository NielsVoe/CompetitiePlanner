# save as app.py
import streamlit as st
from pages.teamPage import TeamPage
import pages.mainPage as mainPage

st.title("Competitie Planner BC Geldrop")

homePage = st.Page("pages/mainPage.py", title="Uitleg")
numberOfTeams = mainPage.GetNumberOfTeams()

for i in range(1, numberOfTeams + 1):
    teamPage = TeamPage(mainPage.GetClub(), f"Team {i}")
    st.sidebar.button(f"Team {i}", on_click=teamPage.DisplayTeam)

pg = st.navigation([homePage] + [teamPage for i in range(1, numberOfTeams + 1)])

pg.run()
