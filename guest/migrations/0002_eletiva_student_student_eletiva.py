# Generated by Django 4.2.4 on 2023-09-19 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guest", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Eletiva",
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
                ("eletiva_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name="student",
            name="student_eletiva",
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
