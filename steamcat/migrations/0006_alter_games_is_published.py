# Generated by Django 5.0 on 2024-01-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steamcat', '0005_tagposts_games_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'DRAFT'), (1, 'PUBLISHED')], default=1),
        ),
    ]
