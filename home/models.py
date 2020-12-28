from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250)

    def __str__(self):
        return self.title


class Movie(models.Model):
    TYPE_CHOICES = (
        ('movie','Movie'),
        ('tv','Tv Series')
    )
    QUALITY_CHOICES = (
        ('hd','HD'),
        ('720','720'),
        ('480','480'),
        ('360','360')
    )
    category = models.ManyToManyField(Category)
    film_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    title = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length = 250,unique=True)
    caption = models.TextField()
    quality = models.CharField(max_length=3,choices=QUALITY_CHOICES)
    year = models.IntegerField(default=2000)
    image = models.URLField()
    views =models.IntegerField(default=0)
    fix = models.BooleanField(default=False)
    translated = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    unlikes = models.IntegerField(default=0)
    

    class Meta:
        ordering = ("-id",)

    def get_absolute_url(self):
        return reverse("movie_detail", args={self.slug})

    def __str__(self):
        return self.title


class Episode(models.Model):
    movie = models.ForeignKey(Movie, related_name='episode', on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 250,unique=True)
    title = models.CharField(max_length=50)
    epi_num = models.IntegerField('Episode number')
    season_num = models.PositiveSmallIntegerField('Season number',blank=True, null=True)
    views =models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    unlikes = models.IntegerField(default=0)

    class Meta:
        ordering = ("-id",)

    def get_absolute_url(self):
        return reverse("episode_detail", args={self.slug})

    def save(self):
        self.title = ' مسلسل ' + str(self.movie.title) + ' الحلقة ' + str(self.epi_num)
        self.slug = slugify(self.movie.slug + ' ' + str(self.season_num) +' ' + str(self.epi_num))
        super(Episode, self).save()

    def __str__(self):
        return self.title

class Link(models.Model):
    LINK_CHOICES = (
        ('download','Download'),
        ('server','Server'),
    )

    episode = models.ForeignKey(Episode,related_name='episode_links', on_delete=models.CASCADE,blank=True, null=True)
    movie = models.ForeignKey(Movie,related_name='movie_links', on_delete=models.CASCADE,blank=True, null=True)
    link_type = models.CharField(max_length=8,choices=LINK_CHOICES,blank=True, null=True)
    name = models.CharField('Server Name',max_length = 250)
    link = models.URLField(max_length = 400,null=True,blank=True)
    iframe = models.CharField(null=True,blank=True,max_length=1000)
    slug = models.SlugField(max_length = 250,unique=True)

    def get_absolute_url(self):
        return reverse('show', args=[self.slug])

    def save(self):
        if self.movie:
            self.slug = slugify(self.movie.slug + ' ' + self.name )
        else:
            self.slug = slugify(self.episode.slug + ' ' + self.name )
        super(Link, self).save()

    def __str__(self):
        return self.name

class Actor(models.Model):
    ACTOR_CHOICES = (
        ('director','Cinematic Director'),
        ('writer','Screenwriter'),
        ('actor','Actor')
    )
    movie = models.ForeignKey(Movie,related_name='movie_actor', on_delete=models.CASCADE)
    actor_type = models.CharField(max_length =8,choices=ACTOR_CHOICES)
    name = models.CharField('Actor Name',max_length =250,unique=True)
    slug = models.SlugField(max_length = 250,unique=True)

    def __str__(self):
        return self.name


class Adds(models.Model):
    ad = models.TextField()
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.active

    class Meta:
        ordering = ("-id",)
    
