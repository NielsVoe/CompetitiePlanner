# save as app.py
import streamlit as st

st.title("Competitie Planner BC Geldrop")

homePage = st.Page("pages/src/mainPage.py", title="Uitleg")

planningPage = st.Page("pages/Planning.py", title="Planning")

# Create a list of team names
team1 = st.Page("pages/BCGeldrop1.py", title="BC Geldrop 1")

pg = st.navigation([homePage, planningPage, team1])

pg.run()
