# Generated by Django 2.1.7 on 2019-04-12 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('address', models.CharField(max_length=512)),
                ('email', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('date_time_created', models.DateTimeField(auto_now_add=True)),
                ('last_checked', models.DateTimeField(auto_now=True)),
                ('health', models.CharField(max_length=1)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FireCheck.building')),
            ],
        ),
        migrations.CreateModel(
            name='panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('name', models.CharField(max_length=128)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FireCheck.building')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('floor', models.IntegerField()),
                ('date_time_created', models.DateTimeField(auto_now_add=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FireCheck.building')),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FireCheck.panel')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='panel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FireCheck.panel'),
        ),
        migrations.AddField(
            model_name='device',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FireCheck.zone'),
        ),
    ]
