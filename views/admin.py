from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Books, Collection, Carts, CartItem

# Register your models here.

class BooksModel(ModelAdmin):
    list_display = ['id','title',"author",'collection']
    list_per_page = 10

class CollectionsModel(ModelAdmin):
    list_display = ['id', 'collection_type']
    list_per_page = 10

class CartsModel(ModelAdmin):
    list_display = ['id', 'items']

admin.site.register(Books, admin_class=BooksModel)
admin.site.register(Collection, admin_class= CollectionsModel) 
admin.site.register(Carts)
admin.site.register(CartItem)