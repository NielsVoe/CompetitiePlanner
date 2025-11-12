import streamlit as st
import datetime

import pages.src.mainPage as MainPage
from src.Team import Team
from src.Teammatch import Teammatch

st.title("Planning")
club = MainPage.GetClub()

youthTeams = ["BC Geldrop J1", "BC Geldrop J2", "BC Geldrop J3", "BC Geldrop J4", "BC Geldrop J5", "BC Geldrop J6"]
seniorTeams = ["BC Geldrop 1", "BC Geldrop 2", "BC Geldrop 3", "BC Geldrop 4", "BC Geldrop 5",
               "BC Geldrop 6", "BC Geldrop 7", "BC Geldrop 8", "BC Geldrop M1"]

teamSelectionCol1, teamSelectionCol2 = st.columns(2)

with teamSelectionCol1:
    allTeamsBtn = st.button("Selecteer alle teams", key="selectAllTeams")
    noTeamsBtn = st.button("Deselecteer alle teams", key="deselectAllTeams")
with teamSelectionCol2:
    youthTeamsBtn = st.button("Selecteer jeugd teams", key="selectYouthTeams")
    seniorTeamsBtn = st.button("Selecteer senioren teams", key="selectSeniorTeams")

if 'defaultTeams' not in st.session_state:
    st.session_state.defaultTeams = []

if allTeamsBtn:
    st.session_state.defaultTeams = youthTeams + seniorTeams
elif noTeamsBtn:
    st.session_state.defaultTeams = []
elif youthTeamsBtn:
    st.session_state.defaultTeams = youthTeams
elif seniorTeamsBtn:
    st.session_state.defaultTeams = seniorTeams

selectedOptions = st.multiselect("Selecteer teams om te tonen in de planning:", 
                                   options=youthTeams + seniorTeams,
                                   default=st.session_state.defaultTeams)

filterChoice = st.radio("Filter wedstrijden op:",
                        options=["Alle wedstrijden", "Thuiswedstrijden", "Uitwedstrijden"],
                        index=0,
                        horizontal=True)

planningButton = st.button("Bekijk wedstrijden", key="planningButton")

startDate = datetime.date(2025, 9, 1) # Startdatum 1 september 2025
endDate = datetime.date(2026, 6, 30) # Einddatum 30 juni 2026
datepicker = st.date_input("Selecteer een datum", 
                           (startDate, endDate),
                            min_value=startDate,
                            max_value=endDate,
                            help="Selecteer een datum tussen 1 september 2025 en 30 juni 2026", 
                            key="datePicker")

if planningButton:
    selectedTeams:list[Team] = []

    for team in selectedOptions:
        selectedTeams.append(club.GetSingleTeam(team.replace("BC Geldrop ", "GELDROP BC ")))
    
    if None in selectedTeams:
        st.rerun()

    teammatches:list[Teammatch] = []
    for team in selectedTeams:
        for match in team.GetMatches():
            if datepicker[0] <= match.GetDate() <= datepicker[1]:
                if filterChoice == "Alle wedstrijden":
                    teammatches.append(match) 
                elif filterChoice == "Thuiswedstrijden" and match.GetHomeTeam() == team.name:
                    teammatches.append(match)
                elif filterChoice == "Uitwedstrijden" and match.GetAwayTeam() == team.name:
                    teammatches.append(match)
    
    if teammatches:
        st.write("Geselecteerde wedstrijden:")
        sortedMatches = sorted(teammatches, key=lambda m: (m.GetDate(), m.GetTime()))
        initialDate = None
        for match in sortedMatches:
            if initialDate is None or match.GetDate() != initialDate:
                initialDate = match.GetDate()
                st.subheader(f"Wedstrijden op {initialDate.strftime('%d-%m-%Y')}")
            st.write(f"{match.GetDay()} om {match.GetTime()}: {match.GetHomeTeam()} vs {match.GetAwayTeam()} - Score: {match.GetScore()[0]}:{match.GetScore()[1]}")
