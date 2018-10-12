from django.urls import include, path
from . import views

urlpatterns = [
    #/TwitterApi/TheSeekers/
    path('TheSeekers/', views.index, name='index'),
    path('TheSeekers/getusertweets', views.get_user_tweets, name='getusertweets'),
    path('TheSeekers/getmentiontweets', views.get_mention_tweets, name='getmentiontweets'),
    path('TheSeekers/getidbasedtweets', views.get_id_based_tweets, name='getidbasedtweets'),
    path('TheSeekers/getfriends', views.get_friends, name='getfriends'),
    # path('TheSeekers/', include('TheSeekers.urls')),
    ]