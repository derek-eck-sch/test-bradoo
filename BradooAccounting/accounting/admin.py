from django.contrib import admin
from .models import Liquidity
from .models import Receivables
from .models import Revenue
from .models import Expenses

# Register your models here.

admin.site.register(Liquidity)
admin.site.register(Receivables)
admin.site.register(Revenue)
admin.site.register(Expenses)