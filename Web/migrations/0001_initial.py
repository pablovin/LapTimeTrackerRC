# Generated by Django 3.1.1 on 2020-09-11 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Car', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lenght', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.car')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.track')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingSessionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('lapNumber', models.IntegerField(default=0)),
                ('lapTime', models.FloatField(default=0)),
                ('speed', models.IntegerField(default=0)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.trainingsession')),
            ],
        ),
    ]
