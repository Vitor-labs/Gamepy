"""Views for inventory app"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from inventory.serializer import GameSerializer
from inventory.models import Game


# TESTED - OK
class GameViewSet(ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_by_genre(self, genre:str = None) -> Response:
        """GET Method endpoint for returning Games for genre
        Args:
            pk (int, optional): Tag name. Defaults to None.
        Returns:
            Response: HTTP response with selected games data
        """
        game = Game.objects.filter(genre=genre)
        serializer = GameSerializer(game, many=True)

        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_by_score(self, score:int = None) -> Response:
        """GET Method endpoint for returning Games for score
        Args:
            pk (int, optional): Tag name. Defaults to None.
        Returns:
            Response: HTTP response with selected games data
        """
        game = Game.objects.filter(score_lte=score).values()
        serializer = GameSerializer(game, many=True)

        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def get_by_price(self, price:int = None) -> Response:
        """GET Method endpoint for returning Games for price
        Args:
            pk (int, optional): Tag name. Defaults to None.
        Returns:
            Response: HTTP response with selected games data
        """
        game = Game.objects.filter(price__gte=price).values()
        serializer = GameSerializer(game, many=True)

        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def get_by_alphabetic(self) -> Response:
        """GET Method endpoint for returning Games for price
        Args:
            pk (int, optional): Tag name. Defaults to None.
        Returns:
            Response: HTTP response with selected games data
        """
        game = Game.objects.all().order_by('name').values()
        serializer = GameSerializer(game, many=True)

        return Response(serializer.data)
