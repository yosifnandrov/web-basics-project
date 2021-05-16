from django.contrib import admin

from django102.models.game import Game
from django102.models.person import Person
from django102.models.player import Player


admin.site.register(Person)
admin.site.register(Game)
admin.site.register(Player)
