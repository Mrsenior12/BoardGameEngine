
from django.urls import path,include
from rest_framework import routers


from . import views
urlpatterns=[
    path('games/getAllGames',views.getAllGames,name='games/getAllGames'),
    path('games/top_10_games',views.top_10_games,name='games/top_10_games'),
    
    path('games/get_games_review',views.get_games_review,name='games/get_games_review'),
    path('games/add_del_review',views.add_del_review,name='games/add_del_review'),

    path('games/populate',views.populateDataBase,name='games/populateDataBase'),
    path('games/search_by_string',views.search_by_string,name='games/search_by_string'),
    path('user/register_user',views.register_user2,name='user/register_user'),
    path('user/login_user',views.login_view2,name='user/login_user'),
    path('user/logout',views.logout_view2,name='user/logout'),
    path('user/check_user_status',views.check_user_status,name='user/check_user_status')
    
    ]