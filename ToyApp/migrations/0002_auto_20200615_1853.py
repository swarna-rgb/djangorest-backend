# Generated by Django 3.0.7 on 2020-06-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='category',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='toy',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
