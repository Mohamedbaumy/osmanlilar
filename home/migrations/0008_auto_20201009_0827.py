# Generated by Django 3.1.2 on 2020-10-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201009_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]