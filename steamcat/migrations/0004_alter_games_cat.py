# Generated by Django 5.0 on 2024-01-13 19:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steamcat', '0003_category_alter_games_slug_games_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='steamcat.category'),
        ),
    ]
