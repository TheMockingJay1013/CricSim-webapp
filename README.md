# CricSim-webapp

A website simulating cricket tournaments, made using HTML, Tailwind CSS and Django

## Features of the website 
This website allows users to :
- Signup to the website
- login / logout
- Start new tournament or continue and existing one
- Simulate the matches 
- View teams, schedule, points table, match scorecards, player stats, team stats and tournament stats


## Installation Steps

### It is recommended to to run this project in a python environment

- Download the files to your device by creating a clone of this project.
  
  On a new terminal , run the command
  ```
  git clone https://github.com/TheMockingJay1013/eMarket.git
  ```
- To install Django run
  ```
  pip install Django
  ```
- Also install django-mathfilters by running 
  ```
  pip install django-mathfilters
  ```
- move to the directory of the project using cd commands

- In the project directory , make the migrations using the commands (This might not be necessary at times)
  ```
  python manage.py makemigrations
  python manage,py migrate
  ```
- Run the server using the command
  ```
  python manage.py runserver
  ```
- Open this link to view the website [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Features to be added in future 
- adding About , Contact , Privacy policy and terms of use pages
- Add animations to UI
- email verification
