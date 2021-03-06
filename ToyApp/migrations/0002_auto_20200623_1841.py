# Generated by Django 3.0.7 on 2020-06-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='toy',
            name='slug',
        ),
    ]
