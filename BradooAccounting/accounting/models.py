from django.db import models

class Liquidity(models.Model):
    liquidityBalance = models.FloatField()

class Receivables(models.Model):
    receivablesBalance = models.FloatField()

class Revenue(models.Model):
    revenueBalance = models.FloatField()

class Expenses(models.Model):
    expensesBalance = models.FloatField()

class Transactions(models.Model):
    id = models.CharField()
    type = models.CharField()
    value = models.FloatField()