from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['uid','name','email','is_active']
    list_filter=['is_active']
    list_editable=['name']
    search_fields=['name','email']
    