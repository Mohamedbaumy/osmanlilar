# Generated by Django 3.1.2 on 2020-10-08 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('epi_num', models.IntegerField(verbose_name='Episode number')),
                ('season_num', models.PositiveSmallIntegerField(verbose_name='Season number')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_type', models.CharField(choices=[('movie', 'Movie'), ('tv', 'Tv Series')], max_length=5)),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('caption', models.TextField()),
                ('quality', models.CharField(choices=[('hd', 'HD'), ('720', '720'), ('480', '480'), ('360', '360')], max_length=3)),
                ('year', models.DateField()),
                ('image', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('fix', models.BooleanField(default=False)),
                ('translated', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('category', models.ManyToManyField(to='home.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_type', models.CharField(choices=[('download', 'Download'), ('server', 'Server'), ('dw_sr', 'Download Server')], max_length=8)),
                ('name', models.CharField(max_length=250, verbose_name='Server Name')),
                ('link', models.URLField(max_length=400)),
                ('episode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episode_links', to='home.episode')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_links', to='home.movie')),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='home.movie'),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_type', models.CharField(choices=[('director', 'Cinematic Director'), ('writer', 'Screenwriter'), ('actor', 'Actor')], max_length=8)),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Actor Name')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_actor', to='home.movie')),
            ],
        ),
    ]
