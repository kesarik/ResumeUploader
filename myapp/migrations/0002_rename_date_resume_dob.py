# Generated by Django 5.0.1 on 2024-02-02 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='date',
            new_name='dob',
        ),
    ]