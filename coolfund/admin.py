from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
from .models import Genre
# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)



class GenreAdmin(MPTTModelAdmin):
    list_display = ('name',)
    # mptt_indent_field = "name"
    # list_display = ('name', 'parent',
    #                 )
    # list_display_links = ('parent',)
    mptt_level_indent = 20


admin.site.register(Genre, GenreAdmin)