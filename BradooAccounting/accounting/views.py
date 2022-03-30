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
    model1 = Liquidity.objects.get(pk=1)
    model2 = Receivables.objects.get(pk=1)
    model3 = Expenses.objects.get(pk=1)
    entries = model1.liquidityBalance + model2.receivablesBalance - model3.expensesBalance
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
    model1 = Receivables.objects.get(pk=1)
    model2 = Expenses.objects.get(pk=1)
    entries = model1.receivablesBalance - model2.expensesBalance
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
                    <h2>Accounting</h2
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
