# Generated by Django 4.2.14 on 2024-08-12 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("learn", "0005_alter_customuser_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(max_length=50),
        ),
    ]
