from django.contrib import admin

# Register your models here.
from .models import shops,shopout,shopput
import xadmin


class UserInfoAdmin(object):
    list_display = ('shop_name', 'shop_number', 'shop_time')

xadmin.site.register(shops, UserInfoAdmin)

class UserInfo(object):
    list_display = ('name',)

xadmin.site.register(shopput, UserInfo)

class UserIn(object):
    list_display = ('name',)

xadmin.site.register(shopout, UserInfo)