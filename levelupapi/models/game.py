from django.db import models
from .game_type import GameType
from .gamer import Gamer


class Game(models.Model):

    gametype = models.ForeignKey(GameType, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=100)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    number_of_players = models.IntegerField(max_length=50)
    skill_level = models.IntegerField(max_length=50)
