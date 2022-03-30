from cgitb import html
from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from accounting.models import Liquidity
from accounting.models import Receivables
from accounting.models import Revenue
from accounting.models import Expenses

# Create your views here.

def index(request):
    html = """<html>
                <body> 
                    <h2>Accounting</h2>
                    <a href='/'>Home  </a>
                    <a href='/liquidity/'>Liquidity  </a>
                    <a href='/receivables/'>Receivables  </a>
                    <a href='/revenue/'>Revenue  </a>
                    <a href='/expenses/'>Expenses  </a> 
                </body>
            </html>"""
    return HttpResponse(html)

def liquidity(request):
    model = Liquidity.objects.get(pk=1)
    entries = model.liquidityBalance
    html = """<html>
                <body> 
                    <h2>Accounting</h2>
                    <a href='/'>Home  </a>
                    <a href='/liquidity/'>Liquidity  </a>
                    <a href='/receivables/'>Receivables  </a>
                    <a href='/revenue/'>Revenue  </a>
                    <a href='/expenses/'>Expenses  </a> 
                    <br>
                    <br> 
                    %s
                </body>
            </html>""" % entries
    return HttpResponse(html)


def receivables(request):
    model = Receivables.objects.get(pk=1)
    entries = model.receivablesBalance
    html = """<html>
                <body> 
                    <h2>Accounting</h2>
                    <a href='/'>Home  </a>
                    <a href='/liquidity/'>Liquidity  </a>
                    <a href='/receivables/'>Receivables  </a>
                    <a href='/revenue/'>Revenue  </a>
                    <a href='/expenses/'>Expenses  </a> 
                    <br>
                    <br> 
                    %s
                </body>
            </html>""" % entries
    return HttpResponse(html)

def revenue(request):
    model = Revenue.objects.get(pk=1)
    entries = model.revenueBalance   
    html = """<html>
                <body> 
                    <h2>Accounting</h2>
                    <a href='/'>Home  </a>
                    <a href='/liquidity/'>Liquidity  </a>
                    <a href='/receivables/'>Receivables  </a>
                    <a href='/revenue/'>Revenue  </a>
                    <a href='/expenses/'>Expenses  </a> 
                    <br>
                    <br> 
                    %s
                </body>
            </html>""" % entries
    return HttpResponse(html) 

def expenses(request):
    model = Expenses.objects.get(pk=1)
    entries = model.expensesBalance
    html = """<html>
                <body>
                    <a href='/'>Home  </a>
                    <a href='/liquidity/'>Liquidity  </a>
                    <a href='/receivables/'>Receivables  </a>
                    <a href='/revenue/'>Revenue  </a>
                    <a href='/expenses/'>Expenses  </a> 
                    <br>
                    <br> 
                    %s
                </body>
            </html>""" % entries
    return HttpResponse(html)
