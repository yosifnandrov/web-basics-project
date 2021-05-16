from django.urls import path

from django102.views import index, UsersListView, GamesListView

urlpatterns = [
    path('', index),
    path('2/', UsersListView.as_view()),
    path('games/', GamesListView.as_view()),
]