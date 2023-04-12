from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_protect 

from nbastats.repository import Repository

import random

repository_name = "nba_stats"
endpoint = "http://127.0.0.1:7200/"
repository = Repository(repository_name, endpoint)


def members(request):
    return render(request, 'startpage.html')


def playersearch(request):

    assert isinstance(request, HttpRequest)

    if "search_text" and "search_season" in request.GET:
        search_text = request.GET["search_text"]
        search_season = request.GET["search_season"]
        if search_text and search_season:

            results = repository.searchPlayers(search_text, search_season)

            tparams = {'results': results, 'search_text': search_text, 'search_season': search_season}

            return render(request, 'players_results.html', tparams)
        else:
            return render(request, 'players_search.html')
    elif "search_text" in request.GET:
        search_text = request.GET["search_text"]
        if search_text:
            results = repository.searchPlayers(search_text, "")

            tparams = {'results': results, 'search_text': search_text, 'search_season': "No season selected"}

            return render(request, 'players_results.html', tparams)
        else:
            return render(request, 'players_search.html')

    return render(request, 'players_search.html')

def topstats(request):

    assert isinstance(request, HttpRequest)

    if "stat" in request.GET:
        stat = request.GET["stat"]
        if stat:

            results = repository.top10OfStat(stat)

            tparams = {'results': results, 'stat': stat}

            return render(request, 'top_stats_results.html', tparams)
        else:
            return render(request, 'top_stats.html')
    
    return render(request, 'top_stats.html')

@csrf_protect
def addplayer(request):

    assert isinstance(request, HttpRequest)

    if "name" and "age" and "league" and "team_code" and "season" and "position" and "points" and "assists" and "games" and "minutes" and "steals" and "blocks" and "threes" and "twos" in request.POST:
        name = request.POST["name"]
        age = request.POST["age"]
        league = request.POST["league"]
        team_code = request.POST["team_code"]
        season = request.POST["season"]
        position = request.POST["position"]
        points = request.POST["points"]
        assists = request.POST["assists"]
        games = request.POST["games"]
        minutes = request.POST["minutes"]
        steals = request.POST["steals"]
        blocks = request.POST["blocks"]
        threes = request.POST["threes"]
        twos = request.POST["twos"]

        if name and age and league and team_code and season and position and points and assists and games and minutes and steals and blocks and threes and twos:

            id = random.randint(6000, 10000)

            results = repository.addPlayer(id, name, age, league, team_code, season, position, points, assists, games, minutes, steals, blocks, threes, twos)

            tparams = {'result': results}

            return render(request, 'add_player.html', tparams)
        else:
            return render(request, 'add_player.html')
    
    return render(request, 'add_player.html')

        
