from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('register',  user_views.register, name = "register"),
]