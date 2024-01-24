from django.db import models
from django.urls import reverse


class Games(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'DRAFT'
        PUBLISHED = 1, 'PUBLISHED'
    game = models.CharField(max_length=255, verbose_name="Гра")
    year = models.IntegerField(blank=True, verbose_name="Рік випуску")
    describe = models.TextField(blank=True,verbose_name="Опис")
    price = models.IntegerField(verbose_name="Ціна")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    url = models.TextField(blank=True,)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)) ,default=Status.PUBLISHED, verbose_name="Стан")
    time_create = models.DateTimeField(auto_now_add=True,verbose_name="Дата публікації статті")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата останнього оновлення статті")
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, related_name='cat', verbose_name="Категорії")
    tags = models.ManyToManyField("TagPosts", blank=True, related_name='tags')

    def __str__(self):
        return self.game

    def __repr__(self):
        return f"\ntitle:{self.game}\nyear:{self.year}"

    def get_absolute_url(self):
        return reverse("finfoaboutgame", kwargs={"game_slug":self.slug})

    class Meta:
        verbose_name="Гра"
        verbose_name_plural="Ігри"

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name="Категорії")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cat_id", kwargs={"cat_id":self.slug})

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

class TagPosts(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_tag_slug", kwargs={"tag_slug":self.slug})