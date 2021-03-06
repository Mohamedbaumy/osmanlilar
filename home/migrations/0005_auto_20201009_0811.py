# Generated by Django 3.1.2 on 2020-10-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201009_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
        migrations.AlterField(
            model_name='episode',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
