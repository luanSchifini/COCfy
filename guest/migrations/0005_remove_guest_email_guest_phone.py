# Generated by Django 4.2.4 on 2023-10-06 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guest", "0004_alter_guest_email"),
    ]

    operations = [
        migrations.RemoveField(model_name="guest", name="email",),
        migrations.AddField(
            model_name="guest",
            name="phone",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
