# Generated by Django 3.1.1 on 2021-05-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phoneNumber',
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.TextField(null=True),
        ),
    ]