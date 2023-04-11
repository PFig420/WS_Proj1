import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef

def create_n_triples(csv_data):
    nba = Namespace('http://example.org/nba/')
    stats = Namespace('http://example.org/nba/stats/')
    xsd = Namespace('http://www.w3.org/2001/XMLSchema#')
    
    g = Graph()
    g.bind('nba', nba)
    g.bind('stats', stats)
    
    for _, row in csv_data.iterrows():
        player_uri = nba[f'player{row["player_id"]}']
        g.add((player_uri, RDF.type, nba.Player))
        g.add((player_uri, nba.player_id, Literal(row['player_id'])))
        g.add((player_uri, nba.player, Literal(row['player'])))
        g.add((player_uri, nba.age, Literal(row['age'])))
        g.add((player_uri, nba.experience, Literal(row['experience'])))
        g.add((player_uri, nba.lg, Literal(row['lg'])))
        
        team_uri = nba[f'team{row["tm"]}']
        g.add((team_uri, RDF.type, nba.Team))
        g.add((team_uri, nba.team_code, Literal(row['tm'])))
        
        stats_uri = stats[f'season{row["season"]}_player{row["player_id"]}']
        g.add((player_uri, nba.has_stats, stats_uri))
        g.add((stats_uri, nba.plays_for, team_uri))
        g.add((stats_uri, RDF.type, stats.SeasonStats))
        g.add((stats_uri, stats.season, Literal(row['season'])))

        g.add((stats_uri, nba.position, Literal(row['pos'])))
        g.add((stats_uri, nba.hasPoints, Literal(row['pts'], datatype=xsd.int)))
        g.add((stats_uri, nba.hasAssists, Literal(row['ast'], datatype=xsd.int)))
        g.add((stats_uri, nba.hasGamesPlayed, Literal(row['g'], datatype=xsd.int)))
        
        if (row['gs'] == "NA"):
            row['gs'] = "Unknown"
            g.add((stats_uri, nba.hasGamesStarted, Literal(row['gs'], datatype=xsd.string)))
        else:
            g.add((stats_uri, nba.hasGamesStarted, Literal(row['gs'], datatype=xsd.int)))

        if (row['mp'] == "NA"):
            row['mp'] = "Unknown"
            g.add((stats_uri, nba.hasMinutesPlayed, Literal(row['mp'], datatype=xsd.string)))
        else:
            g.add((stats_uri, nba.hasMinutesPlayed, Literal(row['mp'], datatype=xsd.int)))

        g.add((stats_uri, nba.hasFieldGoals, Literal(row['fg'], datatype=xsd.int)))

        g.add((stats_uri, nba.hasFieldGoalAttempts, Literal(row['fga'], datatype=xsd.int)))

        if (row['fg_percent'] == "NA"):
            row['fg_percent'] = "Unknown"
            g.add((stats_uri, nba.hasFieldGoalPercentage, Literal(row['fg_percent'], datatype=xsd.string)))
        else:
            g.add((stats_uri, nba.hasFieldGoalPercentage, Literal(row['fg_percent'], datatype=xsd.float)))

        g.add((stats_uri, nba.hasFreeThrows, Literal(row['ft'], datatype=xsd.int)))

        g.add((stats_uri, nba.hasFreeThrowAttempts, Literal(row['fta'], datatype=xsd.int)))

        if (row['ft_percent'] == "NA"):
            row['ft_percent'] = "Unknown"
            g.add((stats_uri, nba.hasFreeThrowPercentage, Literal(row['ft_percent'], datatype=xsd.string)))
        else:
            g.add((stats_uri, nba.hasFreeThrowPercentage, Literal(row['ft_percent'], datatype=xsd.float)))

        if (row['orb'] == "NA"):
            row['orb'] = "Unknown"
            g.add((stats_uri, nba.hasOffensiveRebounds, Literal(row['orb'], datatype=xsd.string)))
        else:   
            g.add((stats_uri, nba.hasOffensiveRebounds, Literal(row['orb'], datatype=xsd.int)))

        if (row['drb'] == "NA"):
            row['drb'] = "Unknown"
            g.add((stats_uri, nba.hasDefensiveRebounds, Literal(row['drb'], datatype=xsd.string)))
        else:
            g.add((stats_uri, nba.hasDefensiveRebounds, Literal(row['drb'], datatype=xsd.int)))

        if (row['trb'] == "NA"):
            row['trb'] = "Unknown"
            g.add((stats_uri, nba.hasTotalRebounds, Literal(row['trb'], datatype=xsd.string)))
        else:
            g.add((stats_uri, nba.hasTotalRebounds, Literal(row['trb'], datatype=xsd.int)))

        if (row['stl'] == "NA"):
            row['stl'] = "Unknown"
            g.add((stats_uri, nba.hasSteals, Literal(row['stl'], datatype=xsd.string)))
        else:
            g.add((stats_uri, nba.hasSteals, Literal(row['stl'], datatype=xsd.int)))

        if (row['blk'] == "NA"):
            row['blk'] = "Unknown"
            g.add((stats_uri, nba.hasBlocks, Literal(row['blk'], datatype=xsd.string)))
        else:    
            g.add((stats_uri, nba.hasBlocks, Literal(row['blk'], datatype=xsd.int)))

        if (row['tov'] == "NA"):
            row['tov'] = "Unknown"
            g.add((stats_uri, nba.hasTurnovers, Literal(row['tov'], datatype=xsd.string)))
        else:  
            g.add((stats_uri, nba.hasTurnovers, Literal(row['tov'], datatype=xsd.int)))

        g.add((stats_uri, nba.hasPersonalFouls, Literal(row['pf'], datatype=xsd.int)))

        if (row['x3p'] == "NA"):
            row['x3p'] = "Unknown"
            g.add((stats_uri, nba.hasThreePointFieldGoals, Literal(row['x3p'], datatype=xsd.string)))
        else:  
            g.add((stats_uri, nba.hasThreePointFieldGoals, Literal(row['x3p'], datatype=xsd.int)))

        if (row['x3pa'] == "NA"):
            row['x3pa'] = "Unknown"
            g.add((stats_uri, nba.hasThreePointFieldGoalAttempts, Literal(row['x3pa'], datatype=xsd.string)))
        else:  
            g.add((stats_uri, nba.hasThreePointFieldGoalAttempts, Literal(row['x3pa'], datatype=xsd.int)))

        if (row['x3p_percent'] == "NA"):
            row['x3p_percent'] = "Unknown"
            g.add((stats_uri, nba.hasThreePointFieldGoalPercentage, Literal(row['x3p_percent'], datatype=xsd.string)))
        else:  
            g.add((stats_uri, nba.hasThreePointFieldGoalPercentage, Literal(row['x3p_percent'], datatype=xsd.float)))

        g.add((stats_uri, nba.hasTwoPointFieldGoals, Literal(row['x2p'], datatype=xsd.int)))
  
        g.add((stats_uri, nba.hasTwoPointFieldGoalAttempts, Literal(row['x2pa'], datatype=xsd.int)))

        if (row['x2p_percent'] == "NA"):
            row['x2p_percent'] = "Unknown"
            g.add((stats_uri, nba.hasTwoPointFieldGoalPercentage, Literal(row['x2p_percent'], datatype=xsd.string)))
        else:  
            g.add((stats_uri, nba.hasTwoPointFieldGoalPercentage, Literal(row['x2p_percent'], datatype=xsd.float)))

    return g

csv_file = 'Player_Totals.csv'
csv_data = pd.read_csv(csv_file)
n_triples_graph = create_n_triples(csv_data)

with open('nba_players_statistics.nt', 'w') as f:
    f.write(n_triples_graph.serialize(format='nt'))
