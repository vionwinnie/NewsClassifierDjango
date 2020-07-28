from django.contrib import admin

# Register your models here.
from .models import News,Category

## Enable admin to edit news type
admin.site.register(News)
admin.site.register(Category)
