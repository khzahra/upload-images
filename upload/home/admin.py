from django.contrib import admin
from .models import UploadImage

# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title', 'body')
    list_filter = ('created', 'updated', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(UploadImage, ImageAdmin)
