from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mtg-home'),
    path('players/', views.PlayerView, name='players'),
    path('player_info/<str:id>', views.PlayerInfo, name='player-info'),
    path('player/<str:id>/edit/', views.PlayerUpdate, name='player-edit'),
    path('player_create/', views.PlayerCreate, name='player-create'),
    path('player/<str:id>/delete', views.PlayerDelete, name='player-delete' ),
    path('matches/', views.MatchView, name='matches'),
    path('match-create/', views.MatchCreate, name='match-create'),
    path('match/<str:id>/delete', views.MatchDelete, name='match-delete'),
    path('match/<str:id>/edit/', views.MatchUpdate, name='match-edit'),
    path('match/<str:id>/turns/', views.TurnView, name='turns'),
    path('turn-create', views.TurnCreate, name='turn-create'),
    path('match/<str:id>/turns/<str:id>/edit/', views.TurnUpdate, name='turn-edit'),
]