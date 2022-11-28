from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user, name='register_user'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name="logout"),
    path('profile', views.profile, name="profile"),
    path('oferta/new', views.crear_oferta, name="crear_oferta"),
    path('oferta/<int:pk>/', views.oferta_detail, name='ofertas_detail'),
    path('home', views.resumen, name='home'),

]