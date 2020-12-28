# Generated by Django 3.1.2 on 2020-12-27 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20201223_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='episode',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('-id',)},
        ),
    ]