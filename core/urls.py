from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm

from . import views

urlpatterns = [
    path('home/<str:tournament>', views.home, name='home'),
    path("", views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('new_tournament/',views.new_tourn,name='new_tourn'),
    path('continue_tournament/',views.continue_tourn,name='continue_tourn'),
    path('show_teams/<str:tournament>',views.show_teams,name='show_teams'),
    path('show_schedule/<str:tournament>',views.show_schedule,name='show_schedule'),
    path('show_points_table/<str:tournament>',views.show_points_table,name='show_points_table'),
    path('simulate/<str:tournament>',views.simulate,name='simulate'),
    path('scorecard/<str:tournament>',views.scorecard,name='scorecard'),
    path("team_stats/<str:tournament>",views.team_stat,name="team_stats"),
]
