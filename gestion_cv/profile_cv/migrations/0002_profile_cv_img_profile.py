# Generated by Django 5.1.1 on 2024-11-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile_cv", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile_cv",
            name="img_profile",
            field=models.ImageField(blank=True, upload_to="profile_images/"),
        ),
    ]