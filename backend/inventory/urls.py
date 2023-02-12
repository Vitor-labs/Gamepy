"""Urls definitions for inventory app"""
from django.urls import path

from rest_framework.renderers import JSONRenderer
from rest_framework.urlpatterns import format_suffix_patterns

from .views import GameViewSet


game_list = GameViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

game_detail = GameViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

game_get_by_genre = GameViewSet.as_view({
    'get': 'get_by_genre'
}, renderer_classes=[JSONRenderer])

game_get_by_score = GameViewSet.as_view({
    'get': 'get_by_score'
}, renderer_classes=[JSONRenderer])

game_get_by_price = GameViewSet.as_view({
    'get': 'get_by_price'
}, renderer_classes=[JSONRenderer])

urlpatterns = format_suffix_patterns([
    path('', game_list, name='game-list'),
    path('<int:pk>/', game_detail, name='game-detail'),
    path('genres/<str:genre>/', game_get_by_genre, name='game-by-genre'),
    path('scores/<int:score>', game_get_by_score, name='game_by_score'),
    path('prices/<int:price>', game_get_by_price, name='game_by_price'),
])
