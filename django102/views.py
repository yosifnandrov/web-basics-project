from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView

from django102.models.game import Game


def index(request):
    title = "CHUSS!"
    users = User.objects.all()
    context = {
        'title': title,
        'users': users,
    }
    return render(request, 'html/index.html', context)


class UsersListView(ListView):
    model = User
    template_name = 'html/index2.html'
    queryset = User.objects.all().order_by('-username')

    def get_context_object_name(self, object_list):
        return 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = "From class view"
        return context


class GamesListView(ListView):
    model = Game
    template_name = 'html/games.html'

    def get_context_object_name(self, object_list):
        return 'games'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = "Games"
        return context
