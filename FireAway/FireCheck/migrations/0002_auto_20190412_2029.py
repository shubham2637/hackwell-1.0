# Generated by Django 2.1.7 on 2019-04-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FireCheck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default='   '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='asada@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=' test', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(default=4564646),
            preserve_default=False,
        ),
    ]
