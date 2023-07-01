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
    
class schedule_table(models.Model) :
    tournament=models.ForeignKey(Tournament,related_name='schedule',on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=100)
    team1=models.CharField(max_length=100)
    team2=models.CharField(max_length=100)
    is_over=models.BooleanField(default=False)
    
class Match(models.Model) :
    schedule=models.ForeignKey(schedule_table,related_name='match',on_delete=models.CASCADE)
    team1_batters=models.CharField(max_length=1000)
    team1_runs=models.CharField(max_length=1000)
    team1_balls=models.CharField(max_length=1000)
    team1_fours=models.CharField(max_length=1000)
    team1_sixes=models.CharField(max_length=1000)
    team1_strike_rates=models.CharField(max_length=1000)
    team2_batters=models.CharField(max_length=1000)
    team2_runs=models.CharField(max_length=1000)
    team2_balls=models.CharField(max_length=1000)
    team2_fours=models.CharField(max_length=1000)
    team2_sixes=models.CharField(max_length=1000)
    team2_strike_rates=models.CharField(max_length=1000)
    team1_bowlers=models.CharField(max_length=1000)
    team1_overs=models.CharField(max_length=1000)
    team1_bowler_runs=models.CharField(max_length=1000)
    team1_wickets=models.CharField(max_length=1000)
    team1_economy=models.CharField(max_length=1000)
    team2_bowlers=models.CharField(max_length=1000)
    team2_overs=models.CharField(max_length=1000)
    team2_bowler_runs=models.CharField(max_length=1000)
    team2_wickets=models.CharField(max_length=1000)
    team2_economy=models.CharField(max_length=1000)
    
    class Meta : 
        verbose_name_plural='Matches'
    
    