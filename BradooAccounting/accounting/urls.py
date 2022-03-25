from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    
    path('liquidity/', views.liquidity, name='liquidity'),
    
    path('receivables/', views.receivables, name='receivables'),
    
    path('revenue/', views.revenue, name='revenue'),

    path('')
]