# Generated by Django 2.2.7 on 2020-03-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='User name')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
            ],
        ),
    ]
