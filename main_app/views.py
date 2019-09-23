from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player, Team 
from .forms import PlayerForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Add the following import
from django.http import HttpResponse

@login_required
def teams_index(request):
    teams = Team.objects.all()
    return render(request, 'teams/index.html', {'teams':teams})

@login_required
def teams_detail(request,team_id):
    team=Team.objects.get(id=team_id)
    user =Team.objects.get
    players=team.player_set.all()
    player_form = PlayerForm()
    return render(request, 'teams/detail.html', {'team':team, 'players': players, 'player_form': player_form})

@login_required
def add_player(request,team_id):
    form = PlayerForm(request.POST)
    if form.is_valid():
        new_player = player.save(commit=False)
        new_player.team_id = team_id
        new_player.save()
    return redirect('detail', team_id = team_id)


class PlayerCreate(LoginRequiredMixin,CreateView):
    model = Player
    fields = '__all__'

    def form_valid(self, form):
        # Assign the logged in user
        form.instance.user = self.request.user
        # Let the CreateView do its job as usual
        return super().form_valid(form)

    

class PlayerUpdate(LoginRequiredMixin,UpdateView):
    model = Player
    fields = ['team','age','points_per_game', 'description']

class PlayerDelete(LoginRequiredMixin, DeleteView):
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


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
