from django.contrib import admin

# Register your models here.
from .models import Product, Service, Student

admin.site.register(Product)

admin.site.register(Service)

admin.site.register(Student)
