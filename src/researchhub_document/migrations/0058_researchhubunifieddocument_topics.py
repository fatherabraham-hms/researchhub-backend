# Generated by Django 4.1 on 2024-05-10 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("topic", "0006_alter_topic_keywords"),
        ("researchhub_document", "0057_alter_researchhubpost_document_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="researchhubunifieddocument",
            name="topics",
            field=models.ManyToManyField(
                blank=True,
                related_name="documents",
                through="topic.UnifiedDocumentTopics",
                to="topic.topic",
            ),
        ),
    ]
