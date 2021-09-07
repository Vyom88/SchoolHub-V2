# Generated by Django 3.1.2 on 2021-08-19 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20210819_1415'),
        ('main', '0005_club_passcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='school',
        ),
        migrations.RemoveField(
            model_name='events',
            name='club_events',
        ),
        migrations.RemoveField(
            model_name='events',
            name='school_events',
        ),
        migrations.DeleteModel(
            name='Announcements',
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.DeleteModel(
            name='School',
        ),
    ]
