# Generated by Django 3.2.23 on 2024-01-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheDailyBugle', '0005_alter_postarticle_article_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postarticle',
            name='article_body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
