from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user, name='register_user'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name="logout"),
    path('home', views.home, name="home"),
    path('profile', views.profile, name="profile"),
    path('edit_profile', views.edit_profile, name="edit_profile")

]