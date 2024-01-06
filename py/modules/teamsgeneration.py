import random
import datetime

class ITeamsGeneration: 
    def _toString(self):
        pass
    def _getTeammates(self):
        pass
    def generate(self):
        pass
    def show(self):
        pass
    def save(self):
        pass

class Local( ITeamsGeneration ):
    def __init__(self, teamsName, numberPerTeam, saveLastTeamsOnly=False):
        self.date = datetime.datetime.now()
        self.teammates = self._getTeammates()
        self.teamsName = teamsName 
        self.numberPerTeam = numberPerTeam
        self.teams = []
        self.saveLastTeamsOnly = saveLastTeamsOnly

    def _getTeammates(self):
        teammates = {}
        with open("teammates", "r") as teammatesFile:
            teammatesName = teammatesFile.readlines()
            id = 0
            for teammateName in teammatesName:
                teammateNameOnUse = teammateName.removesuffix('\n')
                teammates.update({id : teammateNameOnUse})
                id+=1
        return teammates
       
    def generate(self):
        teammatesIdsList = list(self.teammates.keys())
        teamLength = self.numberPerTeam
        teams = []
        teammatesIdsListLength = len(teammatesIdsList)
        if teamLength > teammatesIdsListLength:
            return -1
        random.shuffle(teammatesIdsList)
        for i in range(0, teammatesIdsListLength, teamLength):
            if ( teammatesIdsListLength - (i+teamLength) < teamLength ):
                teams.append(teammatesIdsList[i:-1])
                break
            else:
                teams.append(teammatesIdsList[i:i + teamLength])
        self.teams = teams

    def _toString(self):
        teams = self.teams
        teammates = self.teammates
        teamsName = self.teamsName

        output = ""
        for teamNumber in range(len(teams)):
            output+=f"{teamsName} #{teamNumber+1}\n"
            for id in teams[teamNumber]:
                output+="* "+teammates[id]+'\n'
            output+='\n'
        return output

    def show(self):
        print(self._toString())

    def save(self):
        date = self.date
        saveLastTeamsOnly = self.saveLastTeamsOnly
        rule = "w" if saveLastTeamsOnly else "a" 
        with open("teammates.save", rule) as savingFile:
            savingFile.write("Date: "+str(date)+"\n\n")
            savingFile.write(self._toString())
            savingFile.write('-'*32+'\n\n')

class Remote ( ITeamsGeneration ):
    pass