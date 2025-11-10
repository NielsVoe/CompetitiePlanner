import streamlit as st
from src import ToernooiHandler as TH
from src.JSONHandler import JSONHandler

st.title("Select competition")
st.write("This is a test page for selecting competitions.")

toernooiHandler = TH.ToernooiHandler()
tournaments = toernooiHandler.GetTournaments()

st.write("Available competitions for the planner. Please select the ones you want to include:")

save = st.button("Save selected competitions")

for tournament in tournaments:
    st.checkbox(tournament["Competition"], key=tournament["Link"])

selectedCompetitions = []
for tournament in tournaments:
    if st.session_state.get(tournament["Link"], False):
        selectedCompetitions.append(tournament)

if save:
    JSONHandler.Export(selectedCompetitions, "data", "selected_competitions.json")
    st.success("Selected competitions saved successfully.")