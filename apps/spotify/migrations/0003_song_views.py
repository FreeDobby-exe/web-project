# Generated by Django 3.0.4 on 2020-03-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
