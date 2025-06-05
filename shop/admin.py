# Register your models here.
from django.contrib import admin
from .models import Product
from django.contrib import admin
from .models import RefurbishedProduct

admin.site.register(RefurbishedProduct)
admin.site.register(Product)
