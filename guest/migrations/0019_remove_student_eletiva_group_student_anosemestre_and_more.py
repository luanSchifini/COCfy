# Generated by Django 4.2.4 on 2024-10-14 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0018_rename_cpf_guest_verification_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='eletiva_group',
        ),
        migrations.AddField(
            model_name='student',
            name='anosemestre',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='registration',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
