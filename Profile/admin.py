from django.contrib import admin
from .models import *
# Register your models here.
class user_status(admin.ModelAdmin):
    list_display=['user','email','slug']
    prepopulated_fields={'slug':['user']}
admin.site.register(profile,user_status)