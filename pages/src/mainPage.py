import streamlit as st
import CompetitiePlanner as CP
from src.Club import Club
from src.Gender import Gender
import pandas as pd
from src.JSONHandler import JSONHandler

# Links naar de club pagina's
seniorUrl = "https://badmintonnederland.toernooi.nl/sport/clubs.aspx?id=39A69CCC-55A7-47C2-A19C-E41728508953"
juniorUrl = "https://badmintonnederland.toernooi.nl/sport/clubs.aspx?id=FF2D14A0-938B-45DB-A51F-63DAEC8F3F63"

st.title("Uitleg Competitie Planner")

st.write("""
Welkom bij de Competitie Planner voor BC Geldrop!
""")
table = st.empty()

def GetNumberOfTeams() -> int:
    teams = CP.GetClub().GetTeams()
    if not teams:
        CP.ResetClub()
        CP.RetrieveData(seniorUrl)
        CP.RetrieveData(juniorUrl)
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

# Check if club data json file is not empty
if not JSONHandler.IsEmpty("data/club.json"):
    try:
        CP.GetClub().FromDict(JSONHandler.Import("data/club.json"))
    except Exception as e:
        st.error(f"Fout bij het laden van clubgegevens: {e}")

refreshData = st.button("Ververs data", key="refreshData")

if refreshData:
    table.empty()
    try:
        CP.ResetClub()
        CP.RetrieveData(seniorUrl)
        CP.RetrieveData(juniorUrl)
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    
    df = pd.DataFrame({
        "Team": [team.name for team in CP.GetClub().GetTeams()],
        "Aantal spelers": [len(team.players) for team in CP.GetClub().GetTeams()]
    })

    table.table(df)

    JSONHandler.Export(CP.GetClub().ToDict(), "data/club.json")