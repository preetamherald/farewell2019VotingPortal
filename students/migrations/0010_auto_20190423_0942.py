# Generated by Django 2.2 on 2019-04-23 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20190423_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetail',
            old_name='Mr_VSIT_Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='Ms_VSIT_Name',
        ),
    ]
