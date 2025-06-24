import streamlit as st
import CompetitiePlanner as CP
from src.Club import Club
from src.Gender import Gender
import pandas as pd

st.title("Uitleg Competitie Planner")

st.write("""
Welkom bij de Competitie Planner voor BC Geldrop!
""")
table = st.empty()

def GetNumberOfTeams() -> int:
    teams = CP.GetClub().GetTeams()
    if not teams:
        CP.RetrieveData()
        teams = CP.GetClub().GetTeams()
    if not teams:  # If still no teams after retrieval, we assume there are none
        st.warning("Er zijn momenteel geen teams beschikbaar. Probeer later opnieuw.")
        return 0
    return len(teams)

def GetClub() -> Club:
    return CP.GetClub()

# Check if the club has teams
if CP.GetClub().GetTeams():
    df = pd.DataFrame({
        "Team": [team.name for team in CP.GetClub().GetTeams()],
        "Aantal spelers": [len(team.players) for team in CP.GetClub().GetTeams()]
    })
    table.table(df)

refreshData = st.button("Ververs data")

if refreshData:
    table.empty()
    try:
        CP.RetrieveData()
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    
    df = pd.DataFrame({
        "Team": [team.name for team in CP.GetClub().GetTeams()],
        "Aantal spelers": [len(team.players) for team in CP.GetClub().GetTeams()]
    })

    table.table(df)