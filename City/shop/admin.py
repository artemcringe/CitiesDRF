from django.contrib import admin
from .models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ("shop_name", "city", "street", "open", "close")


admin.site.register(Street)
admin.site.register(Shop, ShopAdmin)
admin.site.register(City)
