# Generated by Django 4.2.4 on 2023-10-08 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("guest", "0010_guest_student_visited"),
    ]

    operations = [
        migrations.RemoveField(model_name="guest", name="student_visited",),
    ]
