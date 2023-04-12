from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

from nbastats.repository import Repository

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


def seasonsearch(request):

    assert isinstance(request, HttpRequest)

    if 'from' in request.POST:

        season = request.POST['from']

        if season and season.isnumeric():

            results = repository.search_year(season)

            return render(request, 'seasons.html', {'from': season, 'base': 'base.html', 'results': results, 'nResults': len(results)})

        
