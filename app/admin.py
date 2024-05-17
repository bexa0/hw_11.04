from django.contrib import admin

from app.models import CustomUser, Category, Product

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Product)
