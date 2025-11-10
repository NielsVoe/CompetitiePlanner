import streamlit as st
import CompetitiePlanner as CP
from src.Club import Club
from src.Gender import Gender
import pandas as pd
from src.JSONHandler import JSONHandler

# Links naar de club pagina's
BASE_URL = "https://badmintonnederland.toernooi.nl/sport/clubs.aspx?id="

st.title("Uitleg Competitie Planner")

st.write("""
Welkom bij de Competitie Planner voor BC Geldrop!
""")
competitionTable = st.empty()
teamTable = st.empty()

def GetCompetitionIDs() -> list[str]:
    try:
        competitions = JSONHandler.Import("data", "selected_competitions.json")
    except Exception as e:
        st.error(f"Error loading competitions: {e}")
        return []
    competitionIDs = [comp["Link"] for comp in competitions]
    return competitionIDs

def GetCompetitionNames() -> list[str]:
    try:
        competitions = JSONHandler.Import("data", "selected_competitions.json")
    except Exception as e:
        st.error(f"Error loading competitions: {e}")
        return []
    competitionNames = [comp["Competition"] for comp in competitions]
    return competitionNames

competitionFrame = pd.DataFrame({
    "Geselecteerde competities": GetCompetitionNames()
})
competitionTable.table(competitionFrame)

def GetClub() -> Club:
    return CP.GetClub()

# Check if the club has teams
if CP.GetClub().GetTeams():
    df = pd.DataFrame({
        "Team": [team.name for team in CP.GetClub().GetTeams()],
        "Aantal spelers": [len(team.players) for team in CP.GetClub().GetTeams()]
    })
    teamTable.table(df)

# Check if club data json file is not empty
if not JSONHandler.IsEmpty("data/club.json"):
    try:
        CP.GetClub().FromDict(JSONHandler.Import("data", "club.json"))
    except Exception as e:
        st.error(f"Fout bij het laden van clubgegevens: {e}")

refreshData = st.button("Ververs data", key="refreshData")

if refreshData:
    teamTable.empty()
    try:
        CP.ResetClub()
        competitionIDs = GetCompetitionIDs()
        for competitionID in competitionIDs:
            CP.RetrieveData(f"{BASE_URL}{competitionID}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    
    df = pd.DataFrame({
        "Team": [team.name for team in CP.GetClub().GetTeams()],
        "Aantal spelers": [len(team.players) for team in CP.GetClub().GetTeams()]
    })

    teamTable.table(df)

    JSONHandler.Export(CP.GetClub().ToDict(), "data", "club.json")