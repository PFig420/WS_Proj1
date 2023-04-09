from graphDBConnection import GraphDB

class Repository:

    #Get the number of players
    nPlayers= """
           PREFIX net:<http://example.org/nba/>
            Select (COUNT(?player) as ?n_players)
                where{
                    ?players net:hasName ?player .
                }	 
    """

    # Get players
    players = """
    PREFIX net:<http://example.org/nba/>
           
    Select ?player ?hasName ?hasPosition ?playsFor ?playsInSeason ?hasPoints ?hasAssists ?hasGamesPlayed ?hasGamesStarted ?hasMinutesPlayed ?hasFieldGoals ?hasFieldGoalAttempts ?hasFieldGoalPercentage ?hasFreeThrows ?hasFreeThrowAttempts ?hasFreeThrowPercentage ?hasOffensiveRebounds ?hasDefensiveRebounds ?hasTotalRebounds ?hasSteals ?hasBlocks ?hasTurnovers ?hasPersonalFouls ?hasThreePointFieldGoals ?hasThreePointFieldGoalAttempts ?hasThreePointFieldGoalPercentage ?hasTwoPointFieldGoals ?hasTwoPointFieldGoalAttempts ?hasTwoPointFieldGoalPercentage
        where{
            ?player net:hasName ?hasName .
            ?player net:hasPosition ?hasPosition .
            ?player net:playsFor ?playsFor .
            ?player net:playsInSeason ?playsInSeason .
            ?player net:hasPoints ?hasPoints .
            ?player net:hasAssists ?hasAssists .
            ?player net:hasGamesPlayed ?hasGamesPlayed .
            ?player net:hasGamesStarted ?hasGamesStarted .
            ?player net:hasMinutesPlayed ?hasMinutesPlayed .
            ?player net:hasFieldGoals ?hasFieldGoals .
            ?player net:hasFieldGoalAttempts ?hasFieldGoalAttempts .
            ?player net:hasFieldGoalPercentage ?hasFieldGoalPercentage .
            ?player net:hasFreeThrows ?hasFreeThrows .
            ?player net:hasFreeThrowAttempts ?hasFreeThrowAttempts .
            ?player net:hasFreeThrowPercentage ?hasFreeThrowPercentage .
            ?player net:hasOffensiveRebounds ?hasOffensiveRebounds .
            ?player net:hasDefensiveRebounds ?hasDefensiveRebounds .
            ?player net:hasTotalRebounds ?hasTotalRebounds .
            ?player net:hasSteals ?hasSteals .
            ?player net:hasBlocks ?hasBlocks .
            ?player net:hasTurnovers ?hasTurnovers .
            ?player net:hasPersonalFouls ?hasPersonalFouls .
            ?player net:hasThreePointFieldGoals ?hasThreePointFieldGoals .
            ?player net:hasThreePointFieldGoalAttempts ?hasThreePointFieldGoalAttempts .
            ?player net:hasThreePointFieldGoalPercentage ?hasThreePointFieldGoalPercentage .
            ?player net:hasTwoPointFieldGoals ?hasTwoPointFieldGoals .
            ?player net:hasTwoPointFieldGoalAttempts ?hasTwoPointFieldGoalAttempts .
            ?player net:hasTwoPointFieldGoalPercentage ?hasTwoPointFieldGoalPercentage .
        }
        Limit 10
    """

    # Get teams
    teams = """
    PREFIX net:<http://example.org/nba/>
    
    Select distinct ?team
        where{
            ?player net:playsFor ?team .
        }
    """  

    def __init__(self, repo_name, endpoint):
        self.graphDB = GraphDB(endpoint, repo_name)

    def getNumberPlayers(self):
        lst = []
        res = self.graphDB.getResults(self.nPlayers)
        for i in res[:5]:
            dic = {}
            dic['n_players'] = i['n_players']['value']
            lst.append(dic)
        return lst
    
    def getPlayers(self):
        lst = []
        res = self.graphDB.getResults(self.players)
        for i in res:
            dic = {}
            dic['hasName'] = i['hasName']['value']
            dic['hasPosition'] = i['hasPosition']['value']
            dic['playsFor'] = i['playsFor']['value']
            dic['playsInSeason'] = i['playsInSeason']['value']
            dic['hasPoints'] = i['hasPoints']['value']
            dic['hasAssists'] = i['hasAssists']['value']
            dic['hasGamesPlayed'] = i['hasGamesPlayed']['value']
            dic['hasGamesStarted'] = i['hasGamesStarted']['value']
            dic['hasMinutesPlayed'] = i['hasMinutesPlayed']['value']
            dic['hasFieldGoals'] = i['hasFieldGoals']['value']
            dic['hasFieldGoalAttempts'] = i['hasFieldGoalAttempts']['value']
            dic['hasFieldGoalPercentage'] = i['hasFieldGoalPercentage']['value']
            dic['hasFreeThrows'] = i['hasFreeThrows']['value']
            dic['hasFreeThrowAttempts'] = i['hasFreeThrowAttempts']['value']
            dic['hasFreeThrowPercentage'] = i['hasFreeThrowPercentage']['value']
            dic['hasOffensiveRebounds'] = i['hasOffensiveRebounds']['value']
            dic['hasDefensiveRebounds'] = i['hasDefensiveRebounds']['value']
            dic['hasTotalRebounds'] = i['hasTotalRebounds']['value']
            dic['hasSteals'] = i['hasSteals']['value']
            dic['hasBlocks'] = i['hasBlocks']['value']
            dic['hasTurnovers'] = i['hasTurnovers']['value']
            dic['hasPersonalFouls'] = i['hasPersonalFouls']['value']
            dic['hasThreePointFieldGoals'] = i['hasThreePointFieldGoals']['value']
            dic['hasThreePointFieldGoalAttempts'] = i['hasThreePointFieldGoalAttempts']['value']
            dic['hasThreePointFieldGoalPercentage'] = i['hasThreePointFieldGoalPercentage']['value']
            dic['hasTwoPointFieldGoals'] = i['hasTwoPointFieldGoals']['value']
            dic['hasTwoPointFieldGoalAttempts'] = i['hasTwoPointFieldGoalAttempts']['value']
            dic['hasTwoPointFieldGoalPercentage'] = i['hasTwoPointFieldGoalPercentage']['value']
            lst.append(dic)
        return lst
    
    def search_season(self, year):
        query_base = "PREFIX net:<http://example.org/nba/> Select ?player ?hasName ?hasPosition ?playsFor ?playsInSeason ?hasPoints ?hasAssists ?hasGamesPlayed ?hasGamesStarted ?hasMinutesPlayed ?hasFieldGoals ?hasFieldGoalAttempts ?hasFieldGoalPercentage ?hasFreeThrows ?hasFreeThrowAttempts ?hasFreeThrowPercentage ?hasOffensiveRebounds ?hasDefensiveRebounds ?hasTotalRebounds ?hasSteals ?hasBlocks ?hasTurnovers ?hasPersonalFouls ?hasThreePointFieldGoals ?hasThreePointFieldGoalAttempts ?hasThreePointFieldGoalPercentage ?hasTwoPointFieldGoals ?hasTwoPointFieldGoalAttempts ?hasTwoPointFieldGoalPercentage where{ ?player net:hasName ?hasName . ?player net:hasPosition ?hasPosition . ?player net:playsFor ?playsFor . ?player net:playsInSeason ?playsInSeason . ?player net:hasPoints ?hasPoints . ?player net:hasAssists ?hasAssists . ?player net:hasGamesPlayed ?hasGamesPlayed . ?player net:hasGamesStarted ?hasGamesStarted . ?player net:hasMinutesPlayed ?hasMinutesPlayed . ?player net:hasFieldGoals ?hasFieldGoals . ?player net:hasFieldGoalAttempts ?hasFieldGoalAttempts . ?player net:hasFieldGoalPercentage ?hasFieldGoalPercentage . ?player net:hasFreeThrows ?hasFreeThrows . ?player net:hasFreeThrowAttempts ?hasFreeThrowAttempts . ?player net:hasFreeThrowPercentage ?hasFreeThrowPercentage . ?player net:hasOffensiveRebounds ?hasOffensiveRebounds . ?player net:hasDefensiveRebounds ?hasDefensiveRebounds . ?player net:hasTotalRebounds ?hasTotalRebounds . ?player net:hasSteals ?hasSteals . ?player net:hasBlocks ?hasBlocks . ?player net:hasTurnovers ?hasTurnovers . ?player net:hasPersonalFouls ?hasPersonalFouls . ?player net:hasThreePointFieldGoals ?hasThreePointFieldGoals . ?player net:hasThreePointFieldGoalAttempts ?hasThreePointFieldGoalAttempts . ?player net:hasThreePointFieldGoalPercentage ?hasThreePointFieldGoalPercentage . ?player net:hasTwoPointFieldGoals ?hasTwoPointFieldGoals . ?player net:hasTwoPointFieldGoalAttempts ?hasTwoPointFieldGoalAttempts . ?player net:hasTwoPointFieldGoalPercentage ?hasTwoPointFieldGoalPercentage . filter(?playsInSeason == '" + year + "')}"
        lst = []
        res = self.graphDB.getResults(query_base)
        for i in res:
            dic = {}
            dic['hasName'] = i['hasName']['value']
            dic['hasPosition'] = i['hasPosition']['value']
            dic['playsFor'] = i['playsFor']['value']
            dic['playsInSeason'] = i['playsInSeason']['value']
            dic['hasPoints'] = i['hasPoints']['value']
            dic['hasAssists'] = i['hasAssists']['value']
            dic['hasGamesPlayed'] = i['hasGamesPlayed']['value']
            dic['hasGamesStarted'] = i['hasGamesStarted']['value']
            dic['hasMinutesPlayed'] = i['hasMinutesPlayed']['value']
            dic['hasFieldGoals'] = i['hasFieldGoals']['value']
            dic['hasFieldGoalAttempts'] = i['hasFieldGoalAttempts']['value']
            dic['hasFieldGoalPercentage'] = i['hasFieldGoalPercentage']['value']
            dic['hasFreeThrows'] = i['hasFreeThrows']['value']
            dic['hasFreeThrowAttempts'] = i['hasFreeThrowAttempts']['value']
            dic['hasFreeThrowPercentage'] = i['hasFreeThrowPercentage']['value']
            dic['hasOffensiveRebounds'] = i['hasOffensiveRebounds']['value']
            dic['hasDefensiveRebounds'] = i['hasDefensiveRebounds']['value']
            dic['hasTotalRebounds'] = i['hasTotalRebounds']['value']
            dic['hasSteals'] = i['hasSteals']['value']
            dic['hasBlocks'] = i['hasBlocks']['value']
            dic['hasTurnovers'] = i['hasTurnovers']['value']
            dic['hasPersonalFouls'] = i['hasPersonalFouls']['value']
            dic['hasThreePointFieldGoals'] = i['hasThreePointFieldGoals']['value']
            dic['hasThreePointFieldGoalAttempts'] = i['hasThreePointFieldGoalAttempts']['value']
            dic['hasThreePointFieldGoalPercentage'] = i['hasThreePointFieldGoalPercentage']['value']
            dic['hasTwoPointFieldGoals'] = i['hasTwoPointFieldGoals']['value']
            dic['hasTwoPointFieldGoalAttempts'] = i['hasTwoPointFieldGoalAttempts']['value']
            dic['hasTwoPointFieldGoalPercentage'] = i['hasTwoPointFieldGoalPercentage']['value']
            lst.append(dic)
        return lst

    def getTeams(self):
        lst = []
        res = self.graphDB.getResults(self.teams)
        for i in res:
            dic = {}
            dic['team'] = i['team']['value']
            lst.append(dic)
        return lst