from django.urls import path

from books import views

urlpatterns = [
    path('', views.index, name="index books"),
    path('create/', views.create_book, name='create book'),
    path('edit/<int:pk>', views.edit_book, name='edit book'),
    path('delete/<int:pk>', views.delete_book, name='delete book'),
]
