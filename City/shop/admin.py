from django.contrib import admin
from .models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ("shop_name", "city", "street", "open", "close")


class StreetAdmin(admin.ModelAdmin):
    list_display = ('street_name', 'city')


admin.site.register(Street, StreetAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(City)
