from django.urls import path

from . import views

urlpatterns=[path('games/getAllGames',views.getAllGames,name='games/getAllGames')]