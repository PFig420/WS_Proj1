'''
Script used to parse the csv data to N-Triples
Authors:
Eduardo Fernandes - 98512
Pedro Figueiredo - 97487
Renato Dias - 98380
'''

import csv
import re
from rdflib import Graph, Namespace, Literal, URIRef

# Define namespaces for RDF
nba = Namespace('http://example.org/nba#')
rdf = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
rdfs = Namespace('http://www.w3.org/2000/01/rdf-schema#')
xsd = Namespace('http://www.w3.org/2001/XMLSchema#')

# Create an RDF graph
g = Graph()

# Load the CSV file
with open('Player_Totals.csv', newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        # Create URIs for the player, team and season
        # player_uri = nba[row['player_id']]
        
        # team_uri = nba[row['tm']]

        # season_uri = nba[row['season']]

        player_uri = URIRef(f'http://example.org/nba/player/{row["player_id"]}')
        team_uri = URIRef(f'http://example.org/nba/team/{row["tm"]}')
        season_uri = URIRef(f'http://example.org/nba/season/{row["season"]}-{int(row["season"]) + 1}')


        
        # Add triples for the player, team and season
        g.add((player_uri, rdf.type, nba.Player))

        g.add((player_uri, nba.hasName, Literal(row['player'], lang='en')))

        g.add((player_uri, nba.hasPosition, Literal(row['pos'], lang='en')))

        g.add((team_uri, rdf.type, nba.Team))

        g.add((team_uri, nba.hasName, Literal(row['tm'], lang='en')))

        # Relate team to a player
        g.add((team_uri, nba.hasPlayer, player_uri))

        g.add((season_uri, rdf.type, nba.Season))

        g.add((season_uri, nba.hasYear, Literal(row['season'], datatype=xsd.int)))

        # Relate season to a player
        g.add((season_uri, nba.hasPlayer, player_uri))

        # Relate player to their team and season
        g.add((player_uri, nba.playsFor, team_uri))

        g.add((player_uri, nba.playsInSeason, season_uri))


        # Add triples for the player's stats
        g.add((player_uri, nba.hasPoints, Literal(row['pts'], datatype=xsd.int)))

        g.add((player_uri, nba.hasAssists, Literal(row['ast'], datatype=xsd.int)))

        g.add((player_uri, nba.hasGamesPlayed, Literal(row['g'], datatype=xsd.int)))

        if (row['gs'] == "NA"):
            row['gs'] = "Unknown"
            g.add((player_uri, nba.hasGamesStarted, Literal(row['gs'], datatype=xsd.string)))
        else:
            g.add((player_uri, nba.hasGamesStarted, Literal(row['gs'], datatype=xsd.int)))

        if (row['mp'] == "NA"):
            row['mp'] = "Unknown"
            g.add((player_uri, nba.hasMinutesPlayed, Literal(row['mp'], datatype=xsd.string)))
        else:
            g.add((player_uri, nba.hasMinutesPlayed, Literal(row['mp'], datatype=xsd.int)))

        g.add((player_uri, nba.hasFieldGoals, Literal(row['fg'], datatype=xsd.int)))

        g.add((player_uri, nba.hasFieldGoalAttempts, Literal(row['fga'], datatype=xsd.int)))

        if (row['fg_percent'] == "NA"):
            row['fg_percent'] = "Unknown"
            g.add((player_uri, nba.hasFieldGoalPercentage, Literal(row['fg_percent'], datatype=xsd.string)))
        else:
            g.add((player_uri, nba.hasFieldGoalPercentage, Literal(row['fg_percent'], datatype=xsd.float)))

        g.add((player_uri, nba.hasFreeThrows, Literal(row['ft'], datatype=xsd.int)))

        g.add((player_uri, nba.hasFreeThrowAttempts, Literal(row['fta'], datatype=xsd.int)))

        if (row['ft_percent'] == "NA"):
            row['ft_percent'] = "Unknown"
            g.add((player_uri, nba.hasFreeThrowPercentage, Literal(row['ft_percent'], datatype=xsd.string)))
        else:
            g.add((player_uri, nba.hasFreeThrowPercentage, Literal(row['ft_percent'], datatype=xsd.float)))

        if (row['orb'] == "NA"):
            row['orb'] = "Unknown"
            g.add((player_uri, nba.hasOffensiveRebounds, Literal(row['orb'], datatype=xsd.string)))
        else:   
            g.add((player_uri, nba.hasOffensiveRebounds, Literal(row['orb'], datatype=xsd.int)))

        if (row['drb'] == "NA"):
            row['drb'] = "Unknown"
            g.add((player_uri, nba.hasDefensiveRebounds, Literal(row['drb'], datatype=xsd.string)))
        else:
            g.add((player_uri, nba.hasDefensiveRebounds, Literal(row['drb'], datatype=xsd.int)))

        if (row['trb'] == "NA"):
            row['trb'] = "Unknown"
            g.add((player_uri, nba.hasTotalRebounds, Literal(row['trb'], datatype=xsd.string)))
        else:
            g.add((player_uri, nba.hasTotalRebounds, Literal(row['trb'], datatype=xsd.int)))

        if (row['stl'] == "NA"):
            row['stl'] = "Unknown"
            g.add((player_uri, nba.hasSteals, Literal(row['stl'], datatype=xsd.string)))
        else:
            g.add((player_uri, nba.hasSteals, Literal(row['stl'], datatype=xsd.int)))

        if (row['blk'] == "NA"):
            row['blk'] = "Unknown"
            g.add((player_uri, nba.hasBlocks, Literal(row['blk'], datatype=xsd.string)))
        else:    
            g.add((player_uri, nba.hasBlocks, Literal(row['blk'], datatype=xsd.int)))

        if (row['tov'] == "NA"):
            row['tov'] = "Unknown"
            g.add((player_uri, nba.hasTurnovers, Literal(row['tov'], datatype=xsd.string)))
        else:  
            g.add((player_uri, nba.hasTurnovers, Literal(row['tov'], datatype=xsd.int)))

        g.add((player_uri, nba.hasPersonalFouls, Literal(row['pf'], datatype=xsd.int)))

        if (row['x3p'] == "NA"):
            row['x3p'] = "Unknown"
            g.add((player_uri, nba.hasThreePointFieldGoals, Literal(row['x3p'], datatype=xsd.string)))
        else:  
            g.add((player_uri, nba.hasThreePointFieldGoals, Literal(row['x3p'], datatype=xsd.int)))

        if (row['x3pa'] == "NA"):
            row['x3pa'] = "Unknown"
            g.add((player_uri, nba.hasThreePointFieldGoalAttempts, Literal(row['x3pa'], datatype=xsd.string)))
        else:  
            g.add((player_uri, nba.hasThreePointFieldGoalAttempts, Literal(row['x3pa'], datatype=xsd.int)))

        if (row['x3p_percent'] == "NA"):
            row['x3p_percent'] = "Unknown"
            g.add((player_uri, nba.hasThreePointFieldGoalPercentage, Literal(row['x3p_percent'], datatype=xsd.string)))
        else:  
            g.add((player_uri, nba.hasThreePointFieldGoalPercentage, Literal(row['x3p_percent'], datatype=xsd.float)))

        g.add((player_uri, nba.hasTwoPointFieldGoals, Literal(row['x2p'], datatype=xsd.int)))
  
        g.add((player_uri, nba.hasTwoPointFieldGoalAttempts, Literal(row['x2pa'], datatype=xsd.int)))

        if (row['x2p_percent'] == "NA"):
            row['x2p_percent'] = "Unknown"
            g.add((player_uri, nba.hasTwoPointFieldGoalPercentage, Literal(row['x2p_percent'], datatype=xsd.string)))
        else:  
            g.add((player_uri, nba.hasTwoPointFieldGoalPercentage, Literal(row['x2p_percent'], datatype=xsd.float)))


# Serialize the graph as N-Triples and write to a file
with open('Player_Totals.nt', 'w') as f:
    f.write(g.serialize(format='nt'))