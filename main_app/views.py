from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player, Team 
from .forms import PlayerForm
# Add the following import
from django.http import HttpResponse

def teams_index(request):
    teams = Team.objects.all()
    return render(request, 'teams/index.html', {'teams':teams})

def teams_detail(request,team_id):
    team=Team.objects.get(id=team_id)
    players=team.player_set.all()
    player_form = PlayerForm()
    return render(request, 'teams/detail.html', {'team':team, 'players': players, 'player_form': player_form})

def add_player(request,team_id):
    form = PlayerForm(request.POST)
    if form.is_valid():
        new_player = player.save(commit=False)
        new_player.team_id = team_id
        new_player.save()
    return redirect('detail', team_id = team_id)


class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'
    

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['team','age','points_per_game', 'description']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def players_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', {'players':players})

def players_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    return render(request, 'players/detail.html', {'player': player})
