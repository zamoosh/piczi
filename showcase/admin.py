from django.contrib import admin
from .models import Picture


class PictureAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price']
    list_editable = ['price', ]
    search_fields = ['name', 'author', 'price']
    ordering = ['name', 'price']
    save_as = True


admin.site.register(Picture, PictureAdmin)
admin.site.site_header = 'Main menu'
admin.site.site_title = 'Admin panel for pictures'
admin.site.index_title = 'admin panel'
