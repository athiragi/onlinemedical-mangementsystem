from django.contrib import admin
from .models import Order, Product,Contact,Feedback

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display= ("name","price","description","image")
admin.site.register(Product,ProductAdmin)
class ContactAdmin(admin.ModelAdmin):
    list_display= ("name","email","phoneno","desc")
admin.site.register(Contact,ContactAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display= ("name","email","items","address","quantity","price","delivery")
admin.site.register(Order,OrderAdmin)
admin.site.register(Feedback)
