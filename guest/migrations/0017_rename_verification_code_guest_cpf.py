# Generated by Django 4.2.4 on 2024-10-14 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0016_student_codigo_alter_guest_verification_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='verification_code',
            new_name='cpf',
        ),
    ]
