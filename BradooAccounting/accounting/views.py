from django.shortcuts import render
from django.http import HttpResponse
import datetime
from accounting.models import Liquidity
from accounting.models import Receivables
from accounting.models import Revenue
from accounting.models import Expenses

# Create your views here.

def index(request):    
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def liquidity():
    all_entries = Liquidity.objects.all()


def receivables():
    all_entries = Receivables.objects.all()

def revenue():
    all_entries = Revenue.objects.all()    

def expenses():
    all_entries = Expenses.objects.all()

def transactions():
    print("helo")
