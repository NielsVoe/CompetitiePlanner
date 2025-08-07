import streamlit as st

import pages.src.mainPage as MainPage

st.title("Planning")

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

planningButton = st.button("Bekijk wedstrijden", key="planningButton")


if planningButton:
    st.write("Je hebt de volgende teams geselecteerd:")
    selected_teams = []
    
    if BCGeldropJ1:
        selected_teams.append("BC Geldrop J1")
    if BCGeldropJ2:
        selected_teams.append("BC Geldrop J2")
    if BCGeldropJ3:
        selected_teams.append("BC Geldrop J3")
    if BCGeldropJ4:
        selected_teams.append("BC Geldrop J4")
    if BCGeldropJ5:
        selected_teams.append("BC Geldrop J5")
    if BCGeldropJ6:
        selected_teams.append("BC Geldrop J6")
    
    if BCGeldrop1:
        selected_teams.append("BC Geldrop 1")
    if BCGeldrop2:
        selected_teams.append("BC Geldrop 2")
    if BCGeldrop3:
        selected_teams.append("BC Geldrop 3")
    if BCGeldrop4:
        selected_teams.append("BC Geldrop 4")
    if BCGeldrop5:
        selected_teams.append("BC Geldrop 5")
    
    if BCGeldrop6:
        selected_teams.append("BC Geldrop 6")
    if BCGeldrop7:
        selected_teams.append("BC Geldrop 7")
    if BCGeldrop8:
        selected_teams.append("BC Geldrop 8")
    if BCGeldropM1:
        selected_teams.append("BC Geldrop M1")

    st.write(", ".join(selected_teams))
    
    # Here you would typically call a function to display the matches for the selected teams