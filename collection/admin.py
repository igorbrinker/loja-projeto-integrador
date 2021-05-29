from django.contrib import admin
from .models import Collection

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name","description")
    prepopulated_fields = {"slug": ("name",)}