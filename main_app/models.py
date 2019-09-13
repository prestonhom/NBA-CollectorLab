from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from datetime import date, time
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators =[MaxValueValidator(50)])
    points_per_game = models.IntegerField(validators =[MaxValueValidator(100)])
    description = models.TextField(max_length=250)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('player_detail', kwargs={'player_id': self.id})

    

class Game(models.Model):
    arena = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    date = models.DateField()
    teams = models.ManyToManyField(Team)
    


    
    

