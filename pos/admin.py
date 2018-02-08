from django.contrib import admin
from .models import MenuInfo

# Register your models here.
class MenuList(admin.ModelAdmin):
    list_display = ('menu_name','url','module','page_name','parent','menu_order','status')
    search_fields = ('menu_name','url','module','page_name','parent','menu_order','status')

admin.site.register(MenuInfo,MenuList)