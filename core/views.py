from django.shortcuts import render,redirect
from .forms import SignupForm,NewTourn
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Tournament,Team,Player,schedule_table,Match
import random
from .schedule import Schedule
from .match import match
from datetime import datetime,timedelta

#classes
class team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.captain = None
class player2:
    
    def __init__(self, name, role):
        self.name=name
        self.role = role
        self.runs_scored=0
        self.balls_faced=0
        self.wickets=0
        self.overs=0
        self.runs_conceded=0

# Create your views here.

def home(request,tournament):
    tournament=Tournament.objects.get(name=tournament,created_by=request.user)
    return render(request, 'home.html',{'tournament':tournament}) 

def index(request):
    return render(request, 'index.html')

def signup(request):
    
    if request.method=='POST' :
         form=SignupForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('login') 
         
    else : 
        form=SignupForm()
    return render(request,'signup.html',{'form':form})  

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def new_tourn(request):
    
    if request.method=='POST' :
        form=NewTourn(request.POST)
        if form.is_valid():
            tournament=form.save(commit=False)
            tournament.created_by=request.user
            tournament.save()
            
            team_names=['Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Deccan Gladiators', 'Jaipur Jaguars', 'Pune Panthers', 'Gujarat Lions', 'Kochi Tuskers Kerala', 'Rising Pune Supergiants', 'Delhi Daredevils', 'Brisbane Heat', 'Adelaide Strikers', 'Melbourne Renegades', 'Melbourne Stars', 'Sydney Sixers', 'Sydney Thunder', 'Perth Scorchers', 'Hobart Hurricanes', 'Big Bash Blasters', 'Canberra Calamities']
            first_name=['Adam', 'John', 'Mike', 'David', 'Steve', 'Daniel', 'Brian', 'Tyler', 'Kevin', 'Jake', 'Eric', 'Tom', 'Luke', 'Jeff', 'Frank', 'Charlie', 'Scott', 'Matt', 'Jack', 'Justin', 'Aarav', 'Aryan', 'Arjun', 'Amit', 'Aniket', 'Ankit', 'Alok', 'Anuj', 'Avinash', 'Aditya', 'Akash', 'Ajit', 'Bharat', 'Bhuvan', 'Brijesh', 'Chirag', 'Chetan', 'Dhruv', 'Dinesh', 'Deepak', 'Dhananjay', 'Dev', 'Devendra', 'Dharmesh', 'Darshan', 'Eklavya', 'Gaurav', 'Gopal', 'Ganesh', 'Hemant', 'Harsh', 'Harshal', 'Hrishikesh', 'Indrajeet', 'Ishaan', 'Jatin', 'Jagdish', 'Kartik', 'Kamal', 'Karan', 'Kunal', 'Krishna', 'Kumar', 'Lalit', 'Lakshya', 'Manish', 'Mukesh', 'Mayank', 'Mahesh', 'Mohan', 'Naveen', 'Nirav', 'Nishant', 'Om', 'Omkar', 'Prashant', 'Pramod', 'Pankaj', 'Parth', 'Pranav', 'Pradeep', 'Piyush', 'Rahul', 'Rakesh', 'Rohit', 'Rajesh', 'Rajendra', 'Sagar', 'Sandeep', 'Saurabh', 'Sanjay', 'Shubham', 'Shreyas', 'Sumit', 'Sushant', 'Siddharth', 'Sudhir', 'Suraj', 'Sushil', 'Sunil', 'Tanmay', 'Tarun', 'Uday', 'Umesh', 'Vikas', 'Vivek', 'Vinay', 'Vaibhav', 'Vikrant', 'Yash', 'Yuvraj']
            last_name=['Smith', 'Johnson', 'Brown', 'Lee', 'Wilson', 'Jones', 'Taylor', 'Clark', 'Wright', 'Walker', 'White', 'Green', 'Hall', 'Baker', 'Lewis', 'Cooper', 'Collins', 'Reed', 'Carter', 'Murphy', 'Agarwal', 'Bhagat', 'Bhargava', 'Chandra', 'Chopra', 'Choudhary', 'Dutta', 'Garg', 'Goyal', 'Gupta', 'Jain', 'Jha', 'Joshi', 'Kapoor', 'Khan', 'Kumar', 'Mahajan', 'Mehra', 'Mishra', 'Nair', 'Patel', 'Puri', 'Raj', 'Rao', 'Sahay', 'Saxena', 'Shah', 'Sharma', 'Singh', 'Sinha', 'Soni', 'Srivastava', 'Thakur', 'Trivedi', 'Verma']
            
            team_list=[]
            while len(team_list)<tournament.no_of_teams :
                y=random.choice(team_names)
                if y not in team_list :
                    team_list.append(y)
            
            for i in range(tournament.no_of_teams) :
                team=Team()
                team.name=team_list[i]
                team.tournament=tournament
                team.save()
                id=team.id
                name=[]
                while len(name)<11 :
                    x=random.choice(first_name) + ' ' + random.choice(last_name)
                    if x not in name :
                        name.append(x)
                    
                for j in range(11):
                    player=Player()
                    player.name=name[j]
                    player.tournament=tournament
                    player.team=team
                    player.role=random.choice(['Batsman','Bowler','All-Rounder','Wicket-Keeper'])
                    player.save()
                captain=random.choice(Player.objects.filter(team=team,tournament=tournament))
                team.captain=captain.name
                team.save()
                
                
            schedule=Schedule()
            venues = ['M. A. Chidambaram Stadium, Chennai', 'Wankhede Stadium, Mumbai', 'Eden Gardens, Kolkata', 'Arun Jaitley Stadium, Delhi', 'M. Chinnaswamy Stadium, Bengaluru', 'Sawai Mansingh Stadium, Jaipur', 'Punjab Cricket Association Stadium, Mohali', 'Rajiv Gandhi International Cricket Stadium, Hyderabad']
            for venue in venues:
                schedule.add_venue(venue)
            
            teams=Team.objects.filter(tournament=tournament)
            for team in teams:
                schedule.add_team(team.name)
            schedule.generate_schedule()
            
            date=datetime(2023,4,14)
            match_count = len(schedule.teams) * (len(schedule.teams) - 1) // 2
            for i in range(len(schedule.matches)):
                if i>=match_count :
                    break
                home,away,venue,date_str,time_str=schedule.matches[i]
                if i%2==0 :
                    date=date+timedelta(days=1)
                    if date.weekday()==5 or date.weekday()==6 :
                        time = datetime.strptime(random.choice(['18:00', '22:00']), "%H:%M")
                    else:
                        time = datetime.strptime('22:00', "%H:%M")
            
                venue = random.choice(schedule.venues)
                while (date.strftime("%d-%m-%Y"), venue) in [(x[3], x[2]) for x in schedule.matches if x]:
                    venue = random.choice(schedule.venues)
                
                new_schedule=schedule_table()
                new_schedule.tournament=tournament
                new_schedule.date=date
                new_schedule.time=time
                new_schedule.venue=venue
                new_schedule.team1=home
                new_schedule.team2=away
                new_schedule.save()
                
                
            return redirect('home',tournament=tournament.name)
    else :
        form=NewTourn()
    return render(request,'new_tourn.html' ,{'form':form})

@login_required
def continue_tourn(request):
    tournaments=Tournament.objects.filter(created_by=request.user)
    return render(request,'continue_tourn.html',{"tournaments":tournaments})

@login_required
def show_teams(request,tournament):
    tournament=Tournament.objects.get(name=tournament,created_by=request.user)
    teams=Team.objects.filter(tournament=tournament)
    team=request.GET.get('team','')
    
    
    if team!='':
        team=Team.objects.get(name=team,tournament=tournament)
        players=Player.objects.filter(team=team,tournament=tournament)
    else :
        players=[]
    return render(request,'show_teams.html',{"teams":teams,"players":players,"tournament":tournament})
    
    
@login_required
def show_schedule(request,tournament):
    tournament=Tournament.objects.get(name=tournament,created_by=request.user)
    schedule=schedule_table.objects.filter(tournament=tournament)
    return render(request,'show_schedule.html',{"schedule":schedule,"tournament":tournament})

@login_required
def show_points_table(request,tournament):
    tournament=Tournament.objects.get(name=tournament,created_by=request.user)
    teams=Team.objects.filter(tournament=tournament)
    teams=teams.order_by('-points').values()
    return render(request,'show_points_table.html',{"teams":teams,"tournament":tournament})

@login_required
def simulate(request,tournament) :
    tournament=Tournament.objects.get(name=tournament,created_by=request.user)
    
    if request.method == 'POST' :
        matches_no=request.POST.get('matches',0)
        matches_no=int(matches_no)
        
        schedule_list=schedule_table.objects.filter(tournament=tournament,is_over=False)[0:matches_no]
        for schedule in schedule_list :
            schedule.is_over=True
            schedule.save()
            team1=Team.objects.get(name=schedule.team1,tournament=tournament)
            team2=Team.objects.get(name=schedule.team2,tournament=tournament)
            team1.played+=1
            team2.played+=1
            
            t1=team(team1.name)
            players=Player.objects.filter(team=team1,tournament=tournament)
            for x in players :
                t1.players.append(player2(x.name,x.role))
            t1.captain=team1.captain
            
            t2=team(team2.name)
            players=Player.objects.filter(team=team2,tournament=tournament)
            for x in players :
                t2.players.append(player2(x.name,x.role))
            t2.captain=team2.captain
            
            m=match(t1,t2)
            m.sim_match(t1,t2)
            
            match_data=Match()
            match_data.schedule=schedule
            
            #Updating the scorecard (match record)
            team1_batters=""
            team1_runs=""
            team1_balls=""
            team1_fours=""
            team1_sixes=""
            team1_sr=""
            team1_bowlers=""
            team1_overs=""
            team1_bowler_runs=""
            team1_wickets=""
            team1_economy=""
            
            for player in m.team1.players :
                match_data.team1_total_runs+=player.batstats.runs 
                if int(player.batstats.balls_faced) > 0 :
                    strike_rate=round(player.batstats.runs/player.batstats.balls_faced*100,2)
                else :
                    strike_rate=0
                strike_rate=str(strike_rate)
                team1_sr=team1_sr + "," + strike_rate
                team1_batters=team1_batters + "," + player.name
                team1_runs=team1_runs + "," + str(player.batstats.runs)
                team1_balls=team1_balls + "," + str(player.batstats.balls_faced)
                team1_fours=team1_fours + "," + str(player.batstats.num_fours)
                team1_sixes=team1_sixes + "," + str(player.batstats.num_sixes)
                
                
                #updating player stat
                player_object=Player.objects.get(team=team1,tournament=tournament,name=player.name)
                player_object.runs_scored += player.batstats.runs 
                player_object.balls_faced += player.batstats.balls_faced 
                player_object.no_fours+=player.batstats.num_fours
                player_object.no_sixes+=player.batstats.num_sixes
                    
                    
                
                
                if int(player.bowlstats.overs)>0 :
                    match_data.team1_total_overs+=player.bowlstats.overs
                    economy=round(player.bowlstats.runs/player.bowlstats.overs,2)
                    economy=str(economy)
                    team1_economy=team1_economy + "," + economy
                    team1_bowlers=team1_bowlers + "," + player.name
                    team1_overs=team1_overs + "," + str(player.bowlstats.overs)
                    team1_bowler_runs=team1_bowler_runs + "," + str(player.bowlstats.runs)
                    team1_wickets=team1_wickets + "," + str(player.bowlstats.wickets)
                    match_data.team1_total_wickets+=player.bowlstats.wickets
                    
                    
                    #updating player bowl stat
                    player_object.wickets+=player.bowlstats.wickets
                    player_object.overs += player.bowlstats.overs
                    player_object.runs_conceded+=player.bowlstats.runs 
                    player_object.save()
            
            match_data.team1_batters=team1_batters
            match_data.team1_runs=team1_runs
            match_data.team1_balls=team1_balls
            match_data.team1_fours=team1_fours
            match_data.team1_sixes=team1_sixes
            match_data.team1_strike_rates=team1_sr
            match_data.team1_bowlers=team1_bowlers
            match_data.team1_overs=team1_overs
            match_data.team1_bowler_runs=team1_bowler_runs
            match_data.team1_wickets=team1_wickets
            match_data.team1_economy=team1_economy
            
            
            
            team2_batters=""
            team2_runs=""
            team2_balls=""
            team2_fours=""
            team2_sixes=""
            team2_sr=""
            team2_bowlers=""
            team2_overs=""
            team2_bowler_runs=""
            team2_wickets=""
            team2_economy=""
            
            for player in m.team2.players :
                match_data.team2_total_runs+=player.batstats.runs 
                if(player.batstats.balls_faced>0):
                    strike_rate=round(player.batstats.runs/player.batstats.balls_faced*100,2)
                else :
                    strike_rate=0
                strike_rate=str(strike_rate)
                team2_sr=team2_sr + "," + strike_rate
                team2_batters=team2_batters + "," + player.name
                team2_runs=team2_runs + "," + str(player.batstats.runs)
                team2_balls=team2_balls + "," + str(player.batstats.balls_faced)
                team2_fours=team2_fours + "," + str(player.batstats.num_fours)
                team2_sixes=team2_sixes + "," + str(player.batstats.num_sixes)
                
                
                #updating player stat
                player_object=Player.objects.get(team=team2,tournament=tournament,name=player.name)
                player_object.runs_scored += player.batstats.runs 
                player_object.balls_faced += player.batstats.balls_faced 
                player_object.no_fours+=player.batstats.num_fours
                player_object.no_sixes+=player.batstats.num_sixes
                
                if player.bowlstats.overs>0 :
                    match_data.team2_total_overs+=player.bowlstats.overs
                    economy=round(player.bowlstats.runs/player.bowlstats.overs,2)
                    economy=str(economy)
                    team2_economy=team2_economy + "," + economy
                    team2_bowlers=team2_bowlers + "," + player.name
                    team2_overs=team2_overs + "," + str(player.bowlstats.overs)
                    team2_bowler_runs=team2_bowler_runs + "," + str(player.bowlstats.runs)
                    team2_wickets=team2_wickets + "," + str(player.bowlstats.wickets)
                    match_data.team2_total_wickets+=player.bowlstats.wickets
                    
                    #updating player bowl stat
                    player_object.wickets+=player.bowlstats.wickets
                    player_object.overs += player.bowlstats.overs
                    player_object.runs_conceded+=player.bowlstats.runs 
                    player_object.save()
            
            match_data.team2_batters=team2_batters
            match_data.team2_runs=team2_runs
            match_data.team2_balls=team2_balls
            match_data.team2_fours=team2_fours
            match_data.team2_sixes=team2_sixes
            match_data.team2_strike_rates=team2_sr
            match_data.team2_bowlers=team2_bowlers
            match_data.team2_overs=team2_overs
            match_data.team2_bowler_runs=team2_bowler_runs
            match_data.team2_wickets=team2_wickets
            match_data.team2_economy=team2_economy
            
            match_data.save()
            
            if match_data.team2_total_runs > match_data.team1_total_runs : 
                team2.won+=1
                team1.lost+=1
                team2.points+=2
                team2.last_5_matches = 'W'+team2.last_5_matches
                team1.last_5_matches='L'+team1.last_5_matches
                
                if len(team2.last_5_matches)>5 :
                    team2.last_5_matches=team2.last_5_matches[:-1]
                if len(team1.last_5_matches)>5 :
                    team1.last_5_matches=team1.last_5_matches[:-1]
                
            if match_data.team2_total_runs < match_data.team1_total_runs : 
                team1.won+=1
                team2.lost+=1
                team1.points+=2
                team2.last_5_matches = 'L'+team2.last_5_matches
                team1.last_5_matches='W'+team1.last_5_matches
                
                if len(team2.last_5_matches)>5 :
                    team2.last_5_matches=team2.last_5_matches[:-1]
                if len(team1.last_5_matches)>5 :
                    team1.last_5_matches=team1.last_5_matches[:-1]
                
            if match_data.team2_total_runs == match_data.team1_total_runs : 
                team2.draw+=1
                team1.draw+=1
                team2.points+=1
                team1.points+=1
                team2.last_5_matches = 'D'+team2.last_5_matches
                team1.last_5_matches='D'+team1.last_5_matches
                
                if len(team2.last_5_matches)>5 :
                    team2.last_5_matches=team2.last_5_matches[:-1]
                if len(team1.last_5_matches)>5 :
                    team1.last_5_matches=team1.last_5_matches[:-1]
                
            team1.save()
            team2.save()
        return redirect('home',tournament=tournament.name)
        
            
    return render(request,'simulate.html',{"tournament":tournament})


@login_required
def scorecard(request,tournament) : 
    tournament=Tournament.objects.get(name=tournament)
    schedules=schedule_table.objects.filter(tournament=tournament,is_over=True)
    selected_match=request.GET.get('match_id',None)
    
    if selected_match:
        schedule_match=schedule_table.objects.get(id=selected_match)
        match=Match.objects.get(schedule=schedule_match)
        team1_batter=match.team1_batters.split(",")[1:]
        team1_runs=match.team1_runs.split(",")[1:]
        team1_balls=match.team1_balls.split(",")[1:]
        team1_fours=match.team1_fours.split(",")[1:]
        team1_sixes=match.team1_sixes.split(",")[1:]
        team1_sr=match.team1_strike_rates.split(",")[1:]
        team1_batting_stat=zip(team1_batter,team1_runs,team1_balls,team1_fours,team1_sixes,team1_sr)
        team1_bowler=match.team1_bowlers.split(",")[1:]
        team1_overs=match.team1_overs.split(",")[1:]
        team1_wickets=match.team1_wickets.split(",")[1:]
        team1_runs_conceded=match.team1_bowler_runs.split(",")[1:]
        team1_economy=match.team1_economy.split(",")[1:]
        team1_bowling_stat=zip(team1_bowler,team1_overs,team1_wickets,team1_runs_conceded,team1_economy)
        team2_batter=match.team2_batters.split(",")[1:]
        team2_runs=match.team2_runs.split(",")[1:]
        team2_balls=match.team2_balls.split(",")[1:]
        team2_fours=match.team2_fours.split(",")[1:]
        team2_sixes=match.team2_sixes.split(",")[1:]
        team2_sr=match.team2_strike_rates.split(",")[1:]
        team2_batting_stat=zip(team2_batter,team2_runs,team2_balls,team2_fours,team2_sixes,team2_sr)
        team2_bowler=match.team2_bowlers.split(",")[1:]
        team2_overs=match.team2_overs.split(",")[1:]
        team2_wickets=match.team2_wickets.split(",")[1:]
        team2_runs_conceded=match.team2_bowler_runs.split(",")[1:]
        team2_economy=match.team2_economy.split(",")[1:]
        team2_bowling_stat=zip(team2_bowler,team2_overs,team2_wickets,team2_runs_conceded,team2_economy)
    else :
        match=None
        schedule_match=None
        team1_batting_stat=[]
        team1_bowling_stat=[]
        team2_batting_stat=[]
        team2_bowling_stat=[]
    return render(request,'scorecard.html',{"selected_match":selected_match,"tournament":tournament,"schedules":schedules,"match":match,"schedule":schedule_match,"team1_batting":team1_batting_stat,"team1_bowling":team1_bowling_stat,"team2_batting":team2_batting_stat,"team2_bowling":team2_bowling_stat})
