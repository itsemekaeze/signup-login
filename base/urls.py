from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.signupPage, name='login'),
    path('register', views.registerUser, name='register'),
    path('logout', views.logoutPage, name='logout'),
]

