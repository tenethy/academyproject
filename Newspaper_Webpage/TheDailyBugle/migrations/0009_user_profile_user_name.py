# Generated by Django 3.2.23 on 2024-01-15 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheDailyBugle', '0008_user_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='user_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
