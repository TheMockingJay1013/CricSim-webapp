from django.shortcuts import render,redirect
from .forms import SignupForm,NewTourn
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Tournament,Team,Player
import random

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
                    player.role=random.choice(['Batsman','Bowler','All Rounder','Wicket Keeper'])
                    player.save()
                captain=random.choice(Player.objects.filter(team=team,tournament=tournament))
                team=Team.objects.filter(id=id)
                team.captain=captain.name
                team.update()
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
    
    