import streamlit as st
from src.Club import Club
from src.Team import Team

class TeamPage:
    def __init__(self, club: Club, teamName: str = ""):
        self.club = club
        self.teamName = teamName

    def DisplayTeam(self):
        teams = self.club.GetTeams()
        team:Team = None
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