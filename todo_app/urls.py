from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="todo index"),
    path('create/', views.create_todo, name="create todo"),
    path('edit/<int:pk>', views.edit_todo, name="edit todo"),
    path('delete/<int:pk>', views.delete_todo, name="delete todo"),
    path('mark_todo_done/<int:pk>', views.mark_todo_done, name='mark todo done')
]