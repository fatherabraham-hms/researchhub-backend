# Generated by Django 2.2.11 on 2020-04-10 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitevisits',
            name='saw_signup_banner',
            field=models.BooleanField(default=False),
        ),
    ]
