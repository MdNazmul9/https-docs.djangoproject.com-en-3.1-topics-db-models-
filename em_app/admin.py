from django.contrib import admin
from .models import Person, Runner
# Register your models here.
admin.site.register([Person, Runner])