from django.contrib import admin
from .models import Category, Client, Product, ClientModel
# Register your models here.




class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    # list_filter = ["created_time", "status", "active"]
    search_fields = ["title"]
    # actions = ["disable_comments", "active_comments"]
    prepopulated_fields={"slug":('title',)}



admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name","description"]
    search_fields = ["name"]
    prepopulated_fields={"slug":('name',)}

admin.site.register(Category, CategoryAdmin)

admin.site.register(ClientModel)




class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'status','phone', 'product',  'address','price']
    list_filter = ["created_time", "status", "active"]
    search_fields = ["name", "id",'phone']
    actions = ["disable_comments", "active_comments"]

    def disable_comments(self, request, queryset):
        queryset.update(active=False)


    def active_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Client, ClientAdmin)
