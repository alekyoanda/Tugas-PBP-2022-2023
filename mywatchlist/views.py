from django.shortcuts import render
from django.http import HttpResponse
from .models import MyWatchList
from django.core import serializers

def index(request):
    return render(request, 'mywatchlist/index.html')

def show_html(request):
    watchlists = MyWatchList.objects.all()
    watched = MyWatchList.objects.filter(watched=True)
    context = {
        'name': 'Alek Yoanda Partogi.T',
        'id': '2106750276',
        'watchlists': watchlists,
        'amount_watched': len(watched),
        'amount_unwatched': len(watchlists) - len(watched)
    }
    return render(request, 'mywatchlist/mywatchlist.html', context)

def show_json(request):
    watchlists = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", watchlists), content_type="application/json")

def show_xml(request):
    watchlists = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", watchlists), content_type="application/xml")