# Generated by Django 2.2.6 on 2019-10-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0012_auto_20191021_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsement',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='flag',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
