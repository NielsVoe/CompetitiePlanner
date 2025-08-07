# save as app.py
import streamlit as st

st.title("Competitie Planner BC Geldrop")

homePage = st.Page("pages/src/mainPage.py", title="Uitleg")

planningPage = st.Page("pages/Planning.py", title="Planning")

# Create a list of team names
team1 = st.Page("pages/BCGeldrop1.py", title="BC Geldrop 1")
team2 = st.Page("pages/BCGeldrop2.py", title="BC Geldrop 2")
team3 = st.Page("pages/BCGeldrop3.py", title="BC Geldrop 3")
team4 = st.Page("pages/BCGeldrop4.py", title="BC Geldrop 4")
team5 = st.Page("pages/BCGeldrop5.py", title="BC Geldrop 5")
team6 = st.Page("pages/BCGeldrop6.py", title="BC Geldrop 6")
team7 = st.Page("pages/BCGeldrop7.py", title="BC Geldrop 7")
team8 = st.Page("pages/BCGeldrop8.py", title="BC Geldrop 8")
teamM1 = st.Page("pages/BCGeldropM1.py", title="BC Geldrop M1")
teamJ1 = st.Page("pages/BCGeldropJ1.py", title="BC Geldrop J1")
teamJ2 = st.Page("pages/BCGeldropJ2.py", title="BC Geldrop J2")
teamJ3 = st.Page("pages/BCGeldropJ3.py", title="BC Geldrop J3")
teamJ4 = st.Page("pages/BCGeldropJ4.py", title="BC Geldrop J4")
teamJ5 = st.Page("pages/BCGeldropJ5.py", title="BC Geldrop J5")
teamJ6 = st.Page("pages/BCGeldropJ6.py", title="BC Geldrop J6")

pg = st.navigation([homePage, planningPage, team1, team2, team3, team4, team5, team6, team7, team8, teamM1, teamJ1, teamJ2, teamJ3, teamJ4, teamJ5, teamJ6])

pg.run()
