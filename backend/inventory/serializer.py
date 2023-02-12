"""Serializers for inventory app"""
from rest_framework.serializers import ModelSerializer

from inventory.models import Game


class GameSerializer(ModelSerializer):
    """Class to define the serializer for game model"""
    class Meta:
        """Game Table metadata"""
        model = Game
        fields = '__all__'
        