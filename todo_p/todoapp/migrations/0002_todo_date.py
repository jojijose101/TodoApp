# Generated by Django 4.2.5 on 2023-09-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default='1999-03-16'),
            preserve_default=False,
        ),
    ]
