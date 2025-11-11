import streamlit as st
from src import ToernooiHandler as TH
from src.JSONHandler import JSONHandler
import bcrypt
import time

st.title("Select competition")
st.write("This is the configuration page for selecting competitions. Please login to continue.")

toernooiHandler = TH.ToernooiHandler()
tournaments = toernooiHandler.GetTournaments()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "auth_expiry" not in st.session_state:
    st.session_state.auth_expiry = 0  # timestamp of expiry

if not st.session_state.get("authenticated"):
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        try:
            with open("data/password.txt", "rb") as f:
                stored_hash = f.read().strip()

            if bcrypt.checkpw(pwd.encode("utf-8"), stored_hash):
                st.session_state.authenticated = True
                st.success("Authenticated successfully.")
                st.session_state.auth_expiry = time.time() + 300  # 5 minutes expiry
                st.rerun()
            else:
                st.error("Incorrect password.")
        except FileNotFoundError:
            st.error("Password file not found.")
else:
    st.write("Available competitions for the planner. Please select the ones you want to include:")

    for tournament in tournaments:
        st.checkbox(tournament["Competition"], key=tournament["Link"])

    save = st.button("Save selected competitions")

    selectedCompetitions = []
    for tournament in tournaments:
        if st.session_state.get(tournament["Link"], False):
            selectedCompetitions.append(tournament)

    if save:
        JSONHandler.Export(selectedCompetitions, "data", "selected_competitions.json")
        st.success("Selected competitions saved successfully.")

    if time.time() > st.session_state.auth_expiry:
        st.session_state.authenticated = False
        st.warning("Session expired.")
        st.rerun()
