from django.db import models
from django.urls import reverse


class Games(models.Model):
    game = models.CharField(max_length=255)
    year = models.IntegerField(blank=True)
    describe = models.TextField(blank=True)
    price = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    url = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"\ntitle:{self.game}\nyear:{self.year}"

    def get_absolute_url(self):
        return reverse("finfoaboutgame", kwargs={"game_slug":self.slug})