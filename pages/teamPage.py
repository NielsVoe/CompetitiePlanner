import streamlit as st

class TeamPage:
    def __init__(self, club, teamName=""):
        self.club = club
        self.teamName = teamName

    def DisplayTeam(self):
        teams = self.club.GetTeams()
        team = None
        for t in teams:
            if t.name == self.teamName:
                team = t
                break
        if team:
            st.subheader(team.name)
            st.write("Players:")
            for player in team.players:
                st.write(f"- {player.name}")
        else:
            st.write("Team not found.")

st.title("Teams")

st.write("This page will display the teams and their players.")