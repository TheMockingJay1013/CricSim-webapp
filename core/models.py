from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tournament(models.Model) :
    name=models.CharField(max_length=100)
    no_of_teams=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='tournament',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Team(models.Model) :
    tournament=models.ForeignKey(Tournament,related_name='team',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    captain=models.CharField(max_length=100,default='')
    played=models.IntegerField(default=0)
    won=models.IntegerField(default=0)
    draw=models.IntegerField(default=0)
    lost=models.IntegerField(default=0)
    points=models.IntegerField(default=0)
    last_5_matches=models.CharField(max_length=100,default='')
        
    
class Player(models.Model) : 
    tournament=models.ForeignKey(Tournament,related_name='player',on_delete=models.CASCADE)
    team=models.ForeignKey(Team,related_name='player',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    runs_scored=models.IntegerField(default=0)
    balls_faced=models.IntegerField(default=0)
    wickets=models.IntegerField(default=0)
    overs=models.IntegerField(default=0)
    runs_conceded=models.IntegerField(default=0)
    
    
    