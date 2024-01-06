from modules.teams import Teams

teams = Teams(teamsName="Groupe", numberPerTeam=3, saveLastTeamsOnly=False)
teams.generateTeams()
teams.showTeams()
teams.backup()