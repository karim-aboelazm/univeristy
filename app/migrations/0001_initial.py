# Generated by Django 4.2.1 on 2023-05-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctors",
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
                ("code", models.CharField(max_length=20)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("certify", models.CharField(max_length=30)),
                ("ssn", models.CharField(max_length=16)),
                ("email", models.EmailField(max_length=254)),
                ("phone_num", models.CharField(max_length=11)),
                (
                    "work_days",
                    models.CharField(
                        choices=[
                            ("i", "i"),
                            ("i", "i"),
                            ("i", "i"),
                            ("i", "i"),
                            ("i", "i"),
                            ("i", "i"),
                        ],
                        max_length=8,
                    ),
                ),
                ("notes", models.TextField()),
                ("spcial", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name_plural": "Doctors",
            },
        ),
    ]
