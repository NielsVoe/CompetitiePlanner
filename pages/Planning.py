import streamlit as st
import datetime

import pages.src.mainPage as MainPage
from src.Team import Team
from src.Teammatch import Teammatch

st.title("Planning")
club = MainPage.GetClub()

youth, senior1, senior2 = st.columns(3)

with youth:
    st.subheader("Jeugd")
    BCGeldropJ1 = st.checkbox("BC Geldrop J1", value=False)
    BCGeldropJ2 = st.checkbox("BC Geldrop J2", value=False)
    BCGeldropJ3 = st.checkbox("BC Geldrop J3", value=False)
    BCGeldropJ4 = st.checkbox("BC Geldrop J4", value=False)
    BCGeldropJ5 = st.checkbox("BC Geldrop J5", value=False)
    BCGeldropJ6 = st.checkbox("BC Geldrop J6", value=False)
with senior1:
    st.subheader("Senioren")
    BCGeldrop1 = st.checkbox("BC Geldrop 1", value=False)
    BCGeldrop2 = st.checkbox("BC Geldrop 2", value=False)
    BCGeldrop3 = st.checkbox("BC Geldrop 3", value=False)
    BCGeldrop4 = st.checkbox("BC Geldrop 4", value=False)
    BCGeldrop5 = st.checkbox("BC Geldrop 5", value=False)
with senior2:
    st.subheader("Senioren")
    BCGeldrop6 = st.checkbox("BC Geldrop 6", value=False)
    BCGeldrop7 = st.checkbox("BC Geldrop 7", value=False)
    BCGeldrop8 = st.checkbox("BC Geldrop 8", value=False)
    BCGeldropM1 = st.checkbox("BC Geldrop M1", value=False)

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
    
    if BCGeldropJ1:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC J1"))
    if BCGeldropJ2:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC J2"))
    if BCGeldropJ3:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC J3"))
    if BCGeldropJ4:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC J4"))
    if BCGeldropJ5:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC J5"))
    if BCGeldropJ6:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC J6"))

    if BCGeldrop1:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC 1"))
    if BCGeldrop2:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC 2"))
    if BCGeldrop3:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC 3"))
    if BCGeldrop4:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC 4"))
    if BCGeldrop5:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC 5"))
    if BCGeldrop6:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC 6"))
    if BCGeldrop7:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC 7"))
    if BCGeldrop8:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC 8"))
    if BCGeldropM1:
        selectedTeams.append(club.GetSingleTeam("GELDROP BC M1"))

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

    
    
    # Here you would typically call a function to display the matches for the selected teams