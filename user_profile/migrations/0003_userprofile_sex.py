# Generated by Django 4.2 on 2024-03-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_userprofile_scope'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.IntegerField(blank=True, choices=[(1, 'Мужской'), (2, 'Женский')], null=True),
        ),
    ]
