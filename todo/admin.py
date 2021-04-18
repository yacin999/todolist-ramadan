from django.contrib import admin
from .models import Todo

# Register your models here.


class Todoadmin(admin.ModelAdmin):
    fields = ["content"]
    filter = ["content"]




admin.site.register(Todo, Todoadmin)
