from modules.teamsgeneration import Local

ltg = Local(
    teamsName="Groupe", 
    numberPerTeam=3, 
    saveLastTeamsOnly=False
    )

ltg.generate()
ltg.show()
ltg.save()