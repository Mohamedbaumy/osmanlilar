# Generated by Django 3.1.2 on 2020-12-23 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20201222_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='iframe',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
    ]
