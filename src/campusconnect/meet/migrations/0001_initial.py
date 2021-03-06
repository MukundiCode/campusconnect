# Generated by Django 3.1.1 on 2021-05-07 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileImage', models.ImageField(blank=True, help_text='Add an picture for your profile', null=True, upload_to='')),
                ('studentNumber', models.IntegerField(default=0, max_length=10)),
                ('phoneNumber', models.IntegerField(max_length=12, null=True)),
                ('description', models.CharField(help_text='Add a brief description about yourself', max_length=200)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]
