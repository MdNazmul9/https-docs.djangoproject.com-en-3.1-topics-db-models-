from django.contrib import admin
# from .models import Person, Group, Membership
# # Register your models here.
# admin.site.register([Person, Group, Membership])

from .models import Blog, Author, Entry
admin.site.register([Blog, Author, Entry])