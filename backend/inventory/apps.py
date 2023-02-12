"""Main configurations for inventory app"""
from django.apps import AppConfig


class InventoryConfig(AppConfig):
    """Class to define the configurations for inventory app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'
