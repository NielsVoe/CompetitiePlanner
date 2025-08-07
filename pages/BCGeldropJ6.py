import streamlit as st
from pages.src.teamPage import TeamPage
import pages.src.mainPage as MainPage
from src.FilterType import FilterType

st.title("BC Geldrop J6")

club = MainPage.GetClub()
teamPage = TeamPage(club, "GELDROP BC J6")

col1, col2, col3 = st.columns(3)
allMatches = col1.button("Alle wedstrijden")
homeMatches = col2.button("Thuiswedstrijden")
awayMatches = col3.button("Uitwedstrijden")

st.write("Players:")
teamPage.DisplayTeam()
st.write("Matches:")

if allMatches:
    teamPage.DisplayMatches(FilterType.ALL)
if homeMatches:
    teamPage.DisplayMatches(FilterType.HOME)
if awayMatches:
    teamPage.DisplayMatches(FilterType.AWAY)