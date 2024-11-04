from django.contrib import admin

# Register your models here.
from .models import Gardens, Owner

admin.site.register(Gardens)
admin.site.register(Owner)
