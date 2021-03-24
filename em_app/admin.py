from django.contrib import admin
from .models import Person, Group, Membership
# Register your models here.
admin.site.register([Person, Group, Membership])