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
            
    SELECT ?player ?name ?team_code ?position ?player_stats ?points ?assists ?stats_season ?games_played ?minutes_played ?blocks ?three_points ?two_points ?steals
    WHERE {
        ?player nba:player ?name .
        ?player nba:has_stats ?player_stats .
        ?player_stats nba:plays_for ?team .
        ?team nba:team_code ?team_code .
        ?player_stats nba:hasPoints ?points .
        ?player_stats nba:hasGamesPlayed ?games_played .
        ?player_stats nba:hasMinutesPlayed ?minutes_played .
        ?player_stats nba:hasBlocks ?blocks .
        ?player_stats nba:hasThreePointFieldGoals ?three_points .
        ?player_stats nba:hasTwoPointFieldGoals ?two_points .
        ?player_stats nba:hasSteals ?steals .
        ?player_stats nba:hasAssists ?assists .
        ?player_stats nba:position ?position .
        ?player_stats stats:season ?stats_season .
        FILTER (regex(?name, "NAME", "i")) .
    """

    # Get top 10 of a stat
    top10_stat = """
    PREFIX nba:<http://example.org/nba/>
    PREFIX stats:<http://example.org/nba/stats/>

    SELECT ?player ?name ?team_code ?position ?player_stats ?points ?assists ?stats_season ?games_played ?minutes_played ?blocks ?three_points ?two_points ?steals
        WHERE {
            ?player nba:player ?name .
            ?player nba:has_stats ?player_stats .
            ?player_stats nba:plays_for ?team .
            ?team nba:team_code ?team_code .
            ?player_stats nba:hasPoints ?points .
            ?player_stats nba:hasGamesPlayed ?games_played .
            ?player_stats nba:hasMinutesPlayed ?minutes_played .
            ?player_stats nba:hasBlocks ?blocks .
            ?player_stats nba:hasThreePointFieldGoals ?three_points .
            ?player_stats nba:hasTwoPointFieldGoals ?two_points .
            ?player_stats nba:hasSteals ?steals .
            ?player_stats nba:hasAssists ?assists .
            ?player_stats nba:position ?position .
            ?player_stats stats:season ?stats_season .
            FILTER (str(?STAT) != "Unknown") .
    }
    ORDER BY DESC(xsd:double(?STAT))
    LIMIT 10
    """

    # Add player
    add_player="""
    PREFIX nba:<http://example.org/nba/>
    PREFIX stats:<http://example.org/nba/stats/>
    PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>

    Insert data{
        nba:playerID nba:type nba:Player;
            nba:player_id "ID"^^xsd:int;
            nba:player "NAME"^^xsd:string;
            nba:age "AGE"^^xsd:int;
            nba:lg "LEAGUE"^^xsd:string;
            nba:has_stats stats:seasonSEAS_playerID.
    
        nba:teamTM_CODE nba:type nba:team;
            nba:team_code "TM_CODE"^^xsd:string.
    
        stats:seasonSEAS_playerID nba:type stats:SeasonStats;
            nba:plays_for nba:teamTM_CODE;
            stats:season "SEAS"^^xsd:int;
            nba:position "POS"^^xsd:string;
            nba:hasPoints "PTS"^^xsd:int;
            nba:hasAssists "AST"^^xsd:int;
            nba:hasGamesPlayed "GMS"^^xsd:int;
            nba:hasMinutesPlayed "MINS"^^xsd:int;
            nba:hasSteals "STLS"^^xsd:int;
            nba:hasBlocks "BLKS"^^xsd:int;
            nba:hasThreePointFieldGoals "3S"^^xsd:int;
            nba:hasTwoPointFieldGoals "2S"^^xsd:int.
    };
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
            dic['season'] = i['stats_season']['value']
            dic['position'] = i['position']['value']
            dic['team_code'] = i['team_code']['value']
            dic['points'] = i['points']['value']
            dic['assists'] = i['assists']['value']
            dic['blocks'] = i['blocks']['value']
            dic['steals'] = i['steals']['value']
            dic['games_played'] = i['games_played']['value']
            dic['minutes_played'] = i['minutes_played']['value']
            dic['three_points'] = i['three_points']['value']
            dic['two_points'] = i['two_points']['value']
            lst.append(dic)

        return lst
    
    def top10OfStat(self, stat):
        top10 = self.top10_stat.replace("STAT", stat)
        lst = []
        res = self.graphDB.getResults(top10)
        for i in res:
            dic = {}
            dic['name'] = i['name']['value']
            dic['season'] = i['stats_season']['value']
            dic['position'] = i['position']['value']
            dic['team_code'] = i['team_code']['value']
            dic['points'] = i['points']['value']
            dic['assists'] = i['assists']['value']
            dic['blocks'] = i['blocks']['value']
            dic['steals'] = i['steals']['value']
            dic['games_played'] = i['games_played']['value']
            dic['minutes_played'] = i['minutes_played']['value']
            dic['three_points'] = i['three_points']['value']
            dic['two_points'] = i['two_points']['value']
            lst.append(dic)

        return lst
    
    def addPlayer(self, id, name , age , league , team_code , season , position , points , assists , games , minutes , steals , blocks , threes , twos):
        player = self.add_player.replace("ID", str(id)).replace("NAME", name).replace("AGE", age).replace("LEAGUE", league).replace("SEAS", season).replace("TM_CODE", team_code).replace("POS", position).replace("PTS", points).replace("AST", assists).replace("GMS", games).replace("MINS", minutes).replace("STLS", steals).replace("BLKS", blocks). replace("3S", threes).replace("2S", twos)
        res = self.graphDB.add(player)
        print(res)
        return res


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