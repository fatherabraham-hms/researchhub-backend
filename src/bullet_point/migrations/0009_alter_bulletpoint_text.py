# Generated by Django 4.1 on 2022-11-11 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bullet_point", "0008_merge_20201119_0123"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bulletpoint",
            name="text",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
