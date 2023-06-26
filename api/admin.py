from django.contrib import admin
from .models import Role, Deperment, Employee

admin.site.register([Role, Deperment, Employee])