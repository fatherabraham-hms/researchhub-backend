# Generated by Django 2.2.14 on 2020-07-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0059_paper_file_created_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='url',
            field=models.URLField(blank=True, default=None, max_length=1024, null=True, unique=True),
        ),
    ]
