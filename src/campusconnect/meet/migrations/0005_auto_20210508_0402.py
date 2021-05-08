# Generated by Django 3.1.1 on 2021-05-08 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('meet', '0004_event_meet_user_meetup'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meet.meetup')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]