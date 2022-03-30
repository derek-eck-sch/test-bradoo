from cgitb import html
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from accounting.models import Liquidity
from accounting.models import Receivables
from accounting.models import Revenue
from accounting.models import Expenses

# Create your views here.

def index(request):    
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def liquidity(request):
    all_entries = Liquidity.objects.all()
    html = "<html><body>%s</body></html>" % all_entries
    return HttpResponse(html)


def receivables(request):
    all_entries = Receivables.objects.all()
    html = "<html><body>%s</body></html>" % all_entries
    return HttpResponse(html)

def revenue(request):
    all_entries = Revenue.objects.all()   
    html = "<html><body>%s</body></html>" % all_entries
    return HttpResponse(html) 

def expenses(request):
    all_entries = Expenses.objects.all()
    html = "<html><body>%s</body></html>" % all_entries
    return HttpResponse(html)
