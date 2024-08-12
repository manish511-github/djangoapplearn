# Generated by Django 4.2.14 on 2024-08-11 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("learn", "0003_alter_customuser_user_type_course"),
    ]

    operations = [
        migrations.CreateModel(
            name="Enrollment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="learn.course"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        limit_choices_to={"user_type": 3},
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("student", "course")},},
        ),
    ]