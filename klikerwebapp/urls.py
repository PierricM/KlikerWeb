from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:pseudo>/game/', views.main_game, name='game'),
    path('ajax/validate_username/$', views.validate_username, name='validate'),
    path('<slug:pseudo>/leaderboard/', views.leaderboard, name='leaderboard'),
]