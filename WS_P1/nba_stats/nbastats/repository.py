from nbastats.graphDBConnection import GraphDB

class Repository:

    #Get the number of players
    nPlayers= """
           PREFIX nba:<http://example.org/nba/>
            Select (COUNT(?player) as ?n_players)
                where{
                    ?players nba:hasName ?player .
                }	 
    """

    # Get players
    players = """
    PREFIX nba:<http://example.org/nba/>
           
    Select ?player ?hasName ?hasPosition ?playsFor ?playsInSeason ?hasPoints ?hasAssists ?hasGamesPlayed ?hasGamesStarted ?hasMinutesPlayed ?hasFieldGoals ?hasFieldGoalAttempts ?hasFieldGoalPercentage ?hasFreeThrows ?hasFreeThrowAttempts ?hasFreeThrowPercentage ?hasOffensiveRebounds ?hasDefensiveRebounds ?hasTotalRebounds ?hasSteals ?hasBlocks ?hasTurnovers ?hasPersonalFouls ?hasThreePointFieldGoals ?hasThreePointFieldGoalAttempts ?hasThreePointFieldGoalPercentage ?hasTwoPointFieldGoals ?hasTwoPointFieldGoalAttempts ?hasTwoPointFieldGoalPercentage
        where{
            ?player nba:hasName ?hasName .
            ?player nba:hasPosition ?hasPosition .
            ?player nba:playsFor ?playsFor .
            ?player nba:playsInSeason ?playsInSeason .
            ?player nba:hasPoints ?hasPoints .
            ?player nba:hasAssists ?hasAssists .
            ?player nba:hasGamesPlayed ?hasGamesPlayed .
            ?player nba:hasGamesStarted ?hasGamesStarted .
            ?player nba:hasMinutesPlayed ?hasMinutesPlayed .
            ?player nba:hasFieldGoals ?hasFieldGoals .
            ?player nba:hasFieldGoalAttempts ?hasFieldGoalAttempts .
            ?player nba:hasFieldGoalPercentage ?hasFieldGoalPercentage .
            ?player nba:hasFreeThrows ?hasFreeThrows .
            ?player nba:hasFreeThrowAttempts ?hasFreeThrowAttempts .
            ?player nba:hasFreeThrowPercentage ?hasFreeThrowPercentage .
            ?player nba:hasOffensiveRebounds ?hasOffensiveRebounds .
            ?player nba:hasDefensiveRebounds ?hasDefensiveRebounds .
            ?player nba:hasTotalRebounds ?hasTotalRebounds .
            ?player nba:hasSteals ?hasSteals .
            ?player nba:hasBlocks ?hasBlocks .
            ?player nba:hasTurnovers ?hasTurnovers .
            ?player nba:hasPersonalFouls ?hasPersonalFouls .
            ?player nba:hasThreePointFieldGoals ?hasThreePointFieldGoals .
            ?player nba:hasThreePointFieldGoalAttempts ?hasThreePointFieldGoalAttempts .
            ?player nba:hasThreePointFieldGoalPercentage ?hasThreePointFieldGoalPercentage .
            ?player nba:hasTwoPointFieldGoals ?hasTwoPointFieldGoals .
            ?player nba:hasTwoPointFieldGoalAttempts ?hasTwoPointFieldGoalAttempts .
            ?player nba:hasTwoPointFieldGoalPercentage ?hasTwoPointFieldGoalPercentage .
        }
        Limit 10
    """

    # Get teams
    teams = """
    PREFIX nba:<http://example.org/nba/>
    
    Select distinct ?team
        where{
            ?player nba:playsFor ?team .
        }
    """  

    # Search players
    search_players = """
    PREFIX nba:<http://example.org/nba/>
    PREFIX stats:<http://example.org/nba/stats/>
            
    SELECT ?player ?name ?team_code ?position ?player_stats ?points ?assists ?stats_season
    WHERE {
        ?player nba:player ?name .
        ?player nba:has_stats ?player_stats .
        ?player_stats nba:plays_for ?team .
        ?team nba:team_code ?team_code .
        ?player_stats nba:hasPoints ?points .
        ?player_stats nba:hasAssists ?assists .
        ?player_stats nba:position ?position .
        ?player_stats stats:season ?stats_season .
        FILTER (regex(?name, "NAME", "i")) .
    """

    # Add player
    """
    PREFIX nba:<http://example.org/nba/>
    PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>

    Insert data{
        nba: nba:hasName "FM";
            nba:hasPosition "FM";
            nba:playsFor "FM";
	        nba:playsInSeason "FM";
	        nba:hasPoints "FM";
            nba:hasAssists "FM";
	        nba:hasGamesPlayed "FM";
	        nba:hasGamesStarted "FM";
            nba:hasMinutesPlayed "FM";
            nba:hasFieldGoals "FM";
            nba:hasFieldGoalAttempts "FM";
            nba:hasFieldGoalPercentage "FM";
            nba:hasFreeThrows "FM";
            nba:hasFreeThrowAttempts "FM";
            nba:hasFreeThrowPercentage "FM";
            nba:hasOffensiveRebounds "FM";
            nba:hasDefensiveRebounds "FM";
            nba:hasTotalRebounds "FM";
            nba:hasSteals "FM";
            nba:hasBlocks "FM";
            nba:hasTurnovers "FM";
            nba:hasPersonalFouls "FM";
            nba:hasThreePointFieldGoals "FM";
            nba:hasThreePointFieldGoalAttempts "FM";
            nba:hasThreePointFieldGoalPercentage "FM";
            nba:hasTwoPointFieldGoals "FM";
            nba:hasTwoPointFieldGoalAttempts "FM";
	        nba:hasTwoPointFieldGoalPercentage "FM".
    }
    """

    def __init__(self, repo_name, endpoint):
        self.graphDB = GraphDB(endpoint, repo_name)

    def searchPlayers(self, search_text, search_season):
        search_players_with_name = self.search_players.replace("NAME", search_text)
        if search_season != "":
            search_players_with_name = search_players_with_name + " filter (?stats_season = " + search_season + " )"
        lst = []
        res = self.graphDB.getResults(search_players_with_name + " }")
        for i in res:
            dic = {}
            dic['name'] = i['name']['value']
            dic['position'] = i['position']['value']
            dic['team_code'] = i['team_code']['value']
            # dic['playsFor'] = i['playsFor']['value']
            # dic['playsInSeason'] = i['playsInSeason']['value']
            dic['points'] = i['points']['value']
            dic['assists'] = i['assists']['value']
            # dic['hasGamesPlayed'] = i['hasGamesPlayed']['value']
            # dic['hasGamesStarted'] = i['hasGamesStarted']['value']
            # dic['hasMinutesPlayed'] = i['hasMinutesPlayed']['value']
            # dic['hasFieldGoals'] = i['hasFieldGoals']['value']
            # dic['hasFieldGoalAttempts'] = i['hasFieldGoalAttempts']['value']
            # dic['hasFieldGoalPercentage'] = i['hasFieldGoalPercentage']['value']
            # dic['hasFreeThrows'] = i['hasFreeThrows']['value']
            # dic['hasFreeThrowAttempts'] = i['hasFreeThrowAttempts']['value']
            # dic['hasFreeThrowPercentage'] = i['hasFreeThrowPercentage']['value']
            # dic['hasOffensiveRebounds'] = i['hasOffensiveRebounds']['value']
            # dic['hasDefensiveRebounds'] = i['hasDefensiveRebounds']['value']
            # dic['hasTotalRebounds'] = i['hasTotalRebounds']['value']
            # dic['hasSteals'] = i['hasSteals']['value']
            # dic['hasBlocks'] = i['hasBlocks']['value']
            # dic['hasTurnovers'] = i['hasTurnovers']['value']
            # dic['hasPersonalFouls'] = i['hasPersonalFouls']['value']
            # dic['hasThreePointFieldGoals'] = i['hasThreePointFieldGoals']['value']
            # dic['hasThreePointFieldGoalAttempts'] = i['hasThreePointFieldGoalAttempts']['value']
            # dic['hasThreePointFieldGoalPercentage'] = i['hasThreePointFieldGoalPercentage']['value']
            # dic['hasTwoPointFieldGoals'] = i['hasTwoPointFieldGoals']['value']
            # dic['hasTwoPointFieldGoalAttempts'] = i['hasTwoPointFieldGoalAttempts']['value']
            # dic['hasTwoPointFieldGoalPercentage'] = i['hasTwoPointFieldGoalPercentage']['value']
            lst.append(dic)

        return lst


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
    
    def searchSeason(self, year):
        query_base = "PREFIX nba:<http://example.org/nba/> Select ?player ?hasName ?hasPosition ?playsFor ?playsInSeason ?hasPoints ?hasAssists ?hasGamesPlayed ?hasGamesStarted ?hasMinutesPlayed ?hasFieldGoals ?hasFieldGoalAttempts ?hasFieldGoalPercentage ?hasFreeThrows ?hasFreeThrowAttempts ?hasFreeThrowPercentage ?hasOffensiveRebounds ?hasDefensiveRebounds ?hasTotalRebounds ?hasSteals ?hasBlocks ?hasTurnovers ?hasPersonalFouls ?hasThreePointFieldGoals ?hasThreePointFieldGoalAttempts ?hasThreePointFieldGoalPercentage ?hasTwoPointFieldGoals ?hasTwoPointFieldGoalAttempts ?hasTwoPointFieldGoalPercentage where{ ?player nba:hasName ?hasName . ?player nba:hasPosition ?hasPosition . ?player nba:playsFor ?playsFor . ?player nba:playsInSeason ?playsInSeason . ?player nba:hasPoints ?hasPoints . ?player nba:hasAssists ?hasAssists . ?player nba:hasGamesPlayed ?hasGamesPlayed . ?player nba:hasGamesStarted ?hasGamesStarted . ?player nba:hasMinutesPlayed ?hasMinutesPlayed . ?player nba:hasFieldGoals ?hasFieldGoals . ?player nba:hasFieldGoalAttempts ?hasFieldGoalAttempts . ?player nba:hasFieldGoalPercentage ?hasFieldGoalPercentage . ?player nba:hasFreeThrows ?hasFreeThrows . ?player nba:hasFreeThrowAttempts ?hasFreeThrowAttempts . ?player nba:hasFreeThrowPercentage ?hasFreeThrowPercentage . ?player nba:hasOffensiveRebounds ?hasOffensiveRebounds . ?player nba:hasDefensiveRebounds ?hasDefensiveRebounds . ?player nba:hasTotalRebounds ?hasTotalRebounds . ?player nba:hasSteals ?hasSteals . ?player nba:hasBlocks ?hasBlocks . ?player nba:hasTurnovers ?hasTurnovers . ?player nba:hasPersonalFouls ?hasPersonalFouls . ?player nba:hasThreePointFieldGoals ?hasThreePointFieldGoals . ?player nba:hasThreePointFieldGoalAttempts ?hasThreePointFieldGoalAttempts . ?player nba:hasThreePointFieldGoalPercentage ?hasThreePointFieldGoalPercentage . ?player nba:hasTwoPointFieldGoals ?hasTwoPointFieldGoals . ?player nba:hasTwoPointFieldGoalAttempts ?hasTwoPointFieldGoalAttempts . ?player nba:hasTwoPointFieldGoalPercentage ?hasTwoPointFieldGoalPercentage . filter(?playsInSeason == '" + year + "')}"
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
    
    def addPlayer(self, id, name, position, team, season, points, assists, games_played, games_started, minutes_played, field_goals, field_goal_attempts, field_goal_percentage, free_throws, free_throw_attempts, free_throw_percentage, offensive_rebounds, defensive_rebounds, total_rebounds, steals, blocks, turnovers, personal_fouls, three_point_goals, three_point_goal_attempts, three_point_goal_percentage, two_point_goals, two_point_goal_attempts, two_point_goal_percentage ):
        query = "PREFIX nba:<http://example.org/nba/> Insert data{ nba:" + id + " nba:hasName '" + name + "'^^xsd:string; nba:hasPosition '" + position + "'^^xsd:string; nba:playsFor '" + team + "'^^xsd:string; nba:playsInSeason '" + season + "'^^xsd:string; nba:hasPoints '" + points + "'^^xsd:string; nba:hasAssists '" + assists + "'^^xsd:string; nba:hasGamesPlayed '" + games_played + "'^^xsd:string; nba:hasGamesStarted '" + games_started + "'^^xsd:string; nba:hasMinutesPlayed '" + minutes_played + "'^^xsd:string; nba:hasFieldGoals '" + field_goals + "'^^xsd:string; nba:hasFieldGoalAttempts '" + field_goal_attempts + "'^^xsd:string; nba:hasFieldGoalPercentage '" + field_goal_percentage + "'^^xsd:string; nba:hasFreeThrows '" + free_throws + "'^^xsd:string; nba:hasFreeThrowAttempts '" + free_throw_attempts + "'^^xsd:string; nba:hasFreeThrowPercentage '" + free_throw_percentage + "'^^xsd:string; nba:hasOffensiveRebounds '" + offensive_rebounds + "'^^xsd:string; nba:hasDefensiveRebounds '" + defensive_rebounds + "'^^xsd:string; nba:hasTotalRebounds '" + total_rebounds + "'^^xsd:string; nba:hasSteals '" + steals + "'^^xsd:string; nba:hasBlocks '" + blocks + "'^^xsd:string; nba:hasTurnovers '" + turnovers + "'^^xsd:string; nba:hasPersonalFouls '" + personal_fouls + "'^^xsd:string; nba:hasThreePointFieldGoals '" + three_point_goals + "'^^xsd:string; nba:hasThreePointFieldGoalAttempts '" + three_point_goal_attempts + "'^^xsd:string; nba:hasThreePointFieldGoalPercentage '" + three_point_goal_percentage + "'^^xsd:string; nba:hasTwoPointFieldGoals '" + two_point_goals + "'^^xsd:string; nba:hasTwoPointFieldGoalAttempts '" + two_point_goal_attempts + "'^^xsd:string; nba:hasTwoPointFieldGoalPercentage '" + two_point_goal_percentage + "'^^xsd:string. }"
        #print(query)
        return self.graphDB.add(query)