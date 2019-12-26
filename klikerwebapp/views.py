from django.http import HttpResponse
from django.shortcuts import render
from .models import Player
import datetime as dt
import pandas as pd

def index(request):
    return render(request, 'klikerweb/game.html', {})


def main_game(request, pseudo):
    try:
        count = request.GET.get('count', None)
        timer = request.GET.get('timer', None)
        person = request.GET.get('person',None)
        print(person)
        print("hello")
        print('timer')
        print(timer)
        print("count status ",count)
    except:
        print('didnt work...')

    if timer!='0':
        return render(request, 'klikerweb/game.html', {})
    else:
        b = Player(pseudo=person, score=count, time=dt.datetime.now())
        b.save()
        return render(request, 'klikerweb/leaderboard.html', {})


def leaderboard(request, pseudo):
    response = "You're looking at the results of question %s."

    df = pd.DataFrame()

    query_results = Player.objects.all()

    df['Pseudo'] = [res.pseudo for res in query_results]
    df['Score'] = [res.score for res in query_results]
    df['Time'] = [res.time.strftime("%m/%d/%Y, %H:%M:%S") for res in query_results]

    def hover(hover_color="#ffff99"):
        return dict(selector="tr:hover",
                    props=[("background-color", "%s" % hover_color)])

    styles = [
        hover(),
        dict(selector="th", props=[("font-size", "150%"),
                                   ("text-align", "center"), ("color", "white")])
    ]

    return render(request, 'klikerweb/leaderboard.html', {'df':df.style.set_table_styles(styles).set_properties(**{'background-color': 'black','color':'white','text-align':'center'}).hide_index().render()})


from django.http import JsonResponse

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': Player.objects.filter(pseudo=username).exists()
    }
    print(data)
    return JsonResponse(data)
