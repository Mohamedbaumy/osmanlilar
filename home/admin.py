from django.contrib import admin
from .models import Category,Actor,Link,Movie,Episode,Adds
# Register your models here.

class ActorInline(admin.StackedInline):
    model = Actor
    raw_id_fields = ['movie']
    extra = 6  
    prepopulated_fields = {'slug':('name',)}  

class LinkInline(admin.StackedInline):
    fields = ('link_type', 'name', 'link','iframe','slug')
    prepopulated_fields = {'slug':('name',)}
    model = Link
    raw_id_fields = ['episode','movie']
    extra = 4 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('category', 'film_type', 'title', 'slug', 'caption', 'quality', 'year', 'image', 'fix', 'translated')
    list_display = ( 'film_type', 'title','quality', 'year', 'views', 'likes','fix', )
    prepopulated_fields = {'slug':('title',)}
    inlines = [ActorInline,LinkInline]

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    fields = ('movie', 'slug', 'title', 'epi_num', 'season_num', )
    list_display =('movie', 'title', 'epi_num', 'season_num', )
    prepopulated_fields = {'slug':('title',)}
    inlines = [LinkInline]

@admin.register(Adds)
class AddsAdmin(admin.ModelAdmin):
    fields = ('ad', 'active' )
    