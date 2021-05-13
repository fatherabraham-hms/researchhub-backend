# Generated by Django 2.2.6 on 2019-11-01 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0004_auto_20191026_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='hub',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hub',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
