"""Admin view for Game model with custom admin view"""
from django.contrib import admin

from inventory.models import Game


class CustomGame(admin.ModelAdmin):
    """Allow to edit Game informations
       list_display = ('name',{'fields':['field']})"""
    fieldsets = [
        ('game', {'fields': ['id','name']}),
        ('info', {'fields': ['price','score','publisher','pub_date']}),
        ('view', {'fields': ['cover','summary','genre']}),
    ]

admin.site.register(Game, CustomGame)
