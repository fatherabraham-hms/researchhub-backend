# Generated by Django 2.2.6 on 2019-11-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0006_auto_20191031_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='summary_plain_text',
            field=models.TextField(default='hello summary'),
            preserve_default=False,
        ),
    ]
