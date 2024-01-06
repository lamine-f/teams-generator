import random
import datetime

class Teams:
    def __init__(self, teamsName, numberPerTeam, saveLastTeamsOnly=False):
        self.date = datetime.datetime.now()
        self.teammates = self.getTeammates()
        self.teamsName = teamsName 
        self.numberPerTeam = numberPerTeam
        self.teams = []
        self.lastTeamsOnly = saveLastTeamsOnly
       
    def generateTeams(self):
        teammatesIdsList = list(self.teammates.keys())
        teamLength = self.numberPerTeam
        teams = []
        teammatesIdsListLength = len(teammatesIdsList)
        if teamLength > teammatesIdsListLength:
            return teams
        random.shuffle(teammatesIdsList)
        for i in range(0, teammatesIdsListLength, teamLength):
            if ( teammatesIdsListLength - (i+teamLength) < teamLength ):
                teams.append(teammatesIdsList[i:-1])
                break
            else:
                teams.append(teammatesIdsList[i:i + teamLength])
        self.teams = teams

    def showTeams(self):
        teams = self.teams
        teammates = self.teammates
        teamsName = self.teamsName
        number = 1
        for team in teams:
            print(f"{teamsName} #{number}")
            for id in team:
                print("* "+teammates[id])
            print("")
            number+=1

    def backup(self):
        date = self.date
        teams = self.teams
        teammates = self.teammates
        teamsName = self.teamsName
        lastTeamsOnly = self.lastTeamsOnly
        rule = "w" if lastTeamsOnly else "a" 
        with open("teammates.save", rule) as backupFile:
            backupFile.write("Date: "+str(date)+"\n\n")
            number = 1
            for team in teams:
                backupFile.write(f" {teamsName} #{number}\n")
                for id in team:
                    backupFile.write(" * "+teammates[id]+'\n')
                backupFile.write("\n")
                number+=1
            backupFile.write('-'*32+'\n\n')

    def getTeammates(self):
        teammates = {}
        with open("teammates", "r") as teammatesFile:
            teammatesName = teammatesFile.readlines()
            id = 0
            for teammateName in teammatesName:
                teammateNameOnUse = teammateName.removesuffix('\n')
                teammates.update({id : teammateNameOnUse})
                id+=1
        return teammates
