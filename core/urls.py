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
]
