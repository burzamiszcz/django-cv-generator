# Generated by Django 4.2.2 on 2023-06-26 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv_generator', '0004_education_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='degree_name',
        ),
    ]
