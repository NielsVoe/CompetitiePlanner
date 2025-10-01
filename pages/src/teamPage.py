import streamlit as st
from src.Club import Club
from src.Team import Team
from src.Gender import Gender
from src.FilterType import FilterType

class TeamPage:
    def __init__(self, club: Club, teamName: str = ""):
        self.club = club
        self.teamName = teamName
        self.team:Team = None
        self.teamDiv:list = []
        self.matchDivs:list = []
    
    def SetTeam(self):
        teams = self.club.GetTeams()
        for team in teams:
            if team.name == self.teamName:
                self.team = team

    def DisplayTeam(self):
        if not self.team:
            self.SetTeam()
        col1, col2 = st.columns(2)
        for player in self.team.players:
            if player.GetGender() is Gender.MALE:
                col1.write(f"**{player.name}**")
            else:
                col2.write(f"**{player.name}**")

    def DisplayMatches(self, filter:FilterType = FilterType.ALL):
        if not self.team:
            self.SetTeam()
        self.matchDivs.clear()
        for match in self.team.GetMatches():
            if filter == FilterType.ALL:
                self.matchDivs.append(st.write(f"{match}"))
            elif filter == FilterType.HOME and match.GetHomeTeam() == self.team.name:
                self.matchDivs.append(st.write(f"{match}"))
            elif filter == FilterType.AWAY and match.GetAwayTeam() == self.team.name:
                self.matchDivs.append(st.write(f"{match}"))