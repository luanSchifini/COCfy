# Generated by Django 4.2.4 on 2023-10-07 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("guest", "0006_remove_guest_phone_guest_email"),
    ]

    operations = [
        migrations.RenameField(
            model_name="eletiva",
            old_name="eletiva_name",
            new_name="eletiva_group_name",
        ),
    ]
