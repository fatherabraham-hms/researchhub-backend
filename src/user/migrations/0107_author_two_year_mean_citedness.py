# Generated by Django 4.1 on 2024-05-17 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0106_authorinstitution"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="two_year_mean_citedness",
            field=models.FloatField(default=0),
        ),
    ]
