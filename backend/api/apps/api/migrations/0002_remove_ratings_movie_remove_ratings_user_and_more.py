# Generated by Django 4.1.3 on 2022-11-13 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='user',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
