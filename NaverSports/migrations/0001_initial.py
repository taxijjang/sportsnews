# Generated by Django 3.0.6 on 2020-05-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NaverSports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('url', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
