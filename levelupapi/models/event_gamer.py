from django.db import models
from .event import Event
from .gamer import Gamer

class Event_Gamer(models.Model):

    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
