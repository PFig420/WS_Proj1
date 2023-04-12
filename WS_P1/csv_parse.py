import pandas as pd
import math
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
        

        if math.isnan(row['gs']):
            row['gs'] = "Unknown"
            g.add((stats_uri, nba.hasGamesStarted, Literal(row['gs'], datatype=xsd.string)))
        else:
            g.add((stats_uri, nba.hasGamesStarted, Literal(row['gs'], datatype=xsd.int)))

        if math.isnan(row['mp']):
            row['mp'] = "Unknown"
            g.add((stats_uri, nba.hasMinutesPlayed, Literal(row['mp'], datatype=xsd.string)))
        else:
            g.add((stats_uri, nba.hasMinutesPlayed, Literal(row['mp'], datatype=xsd.int)))
        
        if math.isnan(row['stl']):
            row['stl'] = "Unknown"
            g.add((stats_uri, nba.hasSteals, Literal(row['stl'])))
        else:
            g.add((stats_uri, nba.hasSteals, Literal(row['stl'], datatype=xsd.integer)))

        if math.isnan(row['blk']):
            row['blk'] = "Unknown"
            g.add((stats_uri, nba.hasBlocks, Literal(row['blk'], datatype=xsd.string)))
        else:    
            g.add((stats_uri, nba.hasBlocks, Literal(row['blk'], datatype=xsd.int)))

        if math.isnan(row['x3p']):
            row['x3p'] = "Unknown"
            g.add((stats_uri, nba.hasThreePointFieldGoals, Literal(row['x3p'], datatype=xsd.string)))
        else:  
            g.add((stats_uri, nba.hasThreePointFieldGoals, Literal(row['x3p'], datatype=xsd.int)))

        if math.isnan(row['x2p']):
            row['x2p'] = "Unknown"
            g.add((stats_uri, nba.hasTwoPointFieldGoals, Literal(row['x2p'], datatype=xsd.string)))
        else:  
            g.add((stats_uri, nba.hasTwoPointFieldGoals, Literal(row['x2p'], datatype=xsd.int)))

    return g

csv_file = 'Player_Totals.csv'
csv_data = pd.read_csv(csv_file)
n_triples_graph = create_n_triples(csv_data)

with open('nba_players_statistics.nt', 'w') as f:
    f.write(n_triples_graph.serialize(format='nt'))
