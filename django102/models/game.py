from django.db import models

from django102.models.player import Player


class Game(models.Model):
    EASY = 0
    MEDIUM = 1
    HARD = 2
    LEVELS_OF_DIFFICULTY_CHOICES = (
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    )
    name = models.CharField(max_length=30)
    level_of_difficulty = models.IntegerField(blank=False, choices=LEVELS_OF_DIFFICULTY_CHOICES)
    players = models.ManyToManyField(Player)
