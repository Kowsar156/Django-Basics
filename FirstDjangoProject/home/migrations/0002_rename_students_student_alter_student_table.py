# Generated by Django 4.2.7 on 2023-11-29 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='students',
            new_name='student',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
