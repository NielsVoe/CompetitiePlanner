import streamlit as st
from pages.TeamPage import TeamPage
import pages.MainPage as MainPage

st.title("BC Geldrop 1")
st.write("Deze pagina toont de spelers van BC Geldrop 1.")

club = MainPage.GetClub()
team = TeamPage(club, "BC Geldrop 1")
if st.button("Ververs data"):
    team.DisplayTeam()