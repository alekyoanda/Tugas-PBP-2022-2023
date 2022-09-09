from django.shortcuts import render
# TODO: Create your views here.
from .models import CatalogItem
def index(request):
    catalog_items = CatalogItem.objects.all()
    context = {
        'name': 'Alek Yoanda Partogi.T',
        'id': '2106750276',
        'catalogs': catalog_items
    }
    return render(request, 'katalog.html', context)