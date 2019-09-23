from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teams/', views.teams_index, name='index'),
    path('teams/<int:team_id>/', views.teams_detail, name='teams_detail'),
    path('teams/<int:team_id>/', views.add_player, name='add_player'),
    path('players/', views.players_index, name='index'),
    path('players/<int:player_id>/', views.players_detail, name='player_detail'),
    path('players/create/', views.PlayerCreate.as_view(),name='players_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
] 

