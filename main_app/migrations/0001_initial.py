# Generated by Django 2.2.3 on 2019-09-11 18:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)])),
                ('points_per_game', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('description', models.TextField(max_length=250)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arena', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=40)),
                ('date', models.DateField()),
                ('teams', models.ManyToManyField(to='main_app.Team')),
            ],
        ),
    ]
