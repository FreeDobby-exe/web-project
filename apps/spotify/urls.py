from django.urls import path, include
from . import views

app_name = 'spotify'
urlpatterns = [
    path('', views.home, name='home'),
    path('top/', views.topSongs, name='top tracks')
]