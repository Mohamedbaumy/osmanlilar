# Generated by Django 3.1.2 on 2020-10-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20201009_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='unlikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='episode',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='unlikes',
            field=models.IntegerField(default=0),
        ),
    ]
