# Generated by Django 2.2.12 on 2020-05-11 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_list', '0015_emailtasklog_notification_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailrecipient',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
