import streamlit as st
from pages.src.teamPage import TeamPage
import pages.src.mainPage as MainPage
from pages.src.teamPage import FilterType

st.title("BC Geldrop 1")

club = MainPage.GetClub()
team = TeamPage(club, "GELDROP BC 1")

col1, col2, col3 = st.columns(3)
allMatches = col1.button("Alle wedstrijden")
homeMatches = col2.button("Thuiswedstrijden")
awayMatches = col3.button("Uitwedstrijden")

st.write("Players:")
team.DisplayTeam()
st.write("Matches:")

if allMatches:
    team.DisplayMatches(FilterType.ALL)
if homeMatches:
    team.DisplayMatches(FilterType.HOME)
if awayMatches:
    team.DisplayMatches(FilterType.AWAY)