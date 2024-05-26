# Generated by Django 4.1 on 2024-05-21 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("paper", "0126_authorship_delete_workauthorship"),
        ("user", "0108_delete_authorcitation"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoAuthor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="coauthor_relationships",
                        to="user.author",
                    ),
                ),
                (
                    "coauthor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="coauthored_with",
                        to="user.author",
                    ),
                ),
                (
                    "paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="coauthorships",
                        to="paper.paper",
                    ),
                ),
            ],
            options={
                "unique_together": {("author", "coauthor", "paper")},
            },
        ),
    ]
