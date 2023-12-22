from django.db import models

class Games(models.Model):
    game = models.CharField(max_length=255)
    year = models.IntegerField(blank=True)
    describe = models.TextField(blank=True)
    price = models.IntegerField()
    url = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
w = Games(game = "ELDEN RING", year = 2022, describe = "THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.", price = 1799, url = "https://store.steampowered.com/app/1245620/ELDEN_RING/")
