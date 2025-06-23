# save as app.py
import streamlit as st
import CompetitiePlanner as CP
from src.Club import Club
from src.Gender import Gender

st.title("Competitie Planner BC Geldrop")

mainPage = st.Page("pages/mainPage.py", title="Uitleg")
teamPage = st.Page("pages/teamPage.py", title="Teams")

pg = st.navigation([mainPage, teamPage])

pg.run()
