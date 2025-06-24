import streamlit as st
from pages.src.teamPage import TeamPage
import pages.src.mainPage as MainPage

st.title("BC Geldrop 1")
st.write("Deze pagina toont de spelers van BC Geldrop 1.")

club = MainPage.GetClub()
team = TeamPage(club, "GELDROP BC 1")
team.DisplayTeam()

if st.button("Ververs data"):
    team.DisplayTeam()