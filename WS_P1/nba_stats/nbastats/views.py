from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

from repository import Repository

repository_name = "nba_stats"
endpoint = "http://127.0.0.1:8000/"
repository = Repository(repository_name, endpoint)


def members(request):
    return render(request, 'startpage.html')


def playersearch(request):

    assert isinstance(request, HttpRequest)

    playersInfo = repository.getPlayers()
    players = len(playersInfo)

    tparams = {
        'players': [],
        'base': 'base.html'
        }
    
    for i in range(players):
        aux = {'hasName': playersInfo[i].get('hasName'), 'hasPosition': playersInfo[i].get('hasPosition'),
               'playsFor': playersInfo[i].get('playsFor'), 'playsInSeason': playersInfo[i].get('playsInSeason'),
               'hasPoints': playersInfo[i].get('hasPoints'), 'hasAssists': playersInfo[i].get('hasAssists'),
               'hasGamesPlayed': playersInfo[i].get('hasGamesPlayed'), 'hasGamesStarted': playersInfo[i].get('hasGamesStarted'),
               'hasMinutesPlayed': playersInfo[i].get('hasMinutesPlayed'), 'hasFieldGoals': playersInfo[i].get('hasFieldGoals'),
               'hasFieldGoalAttempts': playersInfo[i].get('hasFieldGoalAttempts'), 'hasFieldGoalPercentage': playersInfo[i].get('hasFieldGoalPercentage'),
               'hasFreeThrows': playersInfo[i].get('hasFreeThrows'), 'hasFreeThrowAttempts': playersInfo[i].get('hasFreeThrowAttempts'),
               'hasFreeThrowPercentage': playersInfo[i].get('hasFreeThrowPercentage'), 'hasOffensiveRebounds': playersInfo[i].get('hasOffensiveRebounds'),
               'hasDefensiveRebounds': playersInfo[i].get('hasDefensiveRebounds'), 'hasTotalRebounds': playersInfo[i].get('hasTotalRebounds'),
               'hasSteals': playersInfo[i].get('hasSteals'), 'hasBlocks': playersInfo[i].get('hasBlocks'),
               'hasTurnovers': playersInfo[i].get('hasTurnovers'), 'hasPersonalFouls': playersInfo[i].get('hasPersonalFouls'),
               'hasThreePointFieldGoals': playersInfo[i].get('hasThreePointFieldGoals'), 'hasThreePointFieldGoalAttempts': playersInfo[i].get('hasThreePointFieldGoalAttempts'),
               'hasThreePointFieldGoalPercentage': playersInfo[i].get('hasThreePointFieldGoalPercentage'), 'hasTwoPointFieldGoals': playersInfo[i].get('hasTwoPointFieldGoals'),
               'hasTwoPointFieldGoalAttempts': playersInfo[i].get('hasTwoPointFieldGoalAttempts'), 'hasTwoPointFieldGoalPercentage': playersInfo[i].get('hasTwoPointFieldGoalPercentage')}

        tparams['players'].append(aux)

    return render(request, 'players.html', tparams)



def seasonsearch(request):

    assert isinstance(request, HttpRequest)

    if 'from' in request.POST:

        season = request.POST['from']

        if season and season.isnumeric():

            results = repository.search_year(season)

            return render(request, 'seasons.html', {'from': season, 'base': 'base.html', 'results': results, 'nResults': len(results)})

        
