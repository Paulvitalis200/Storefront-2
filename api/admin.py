from django.contrib import admin
from api.models import Order, OrderItem, User, Product

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline
    ] # Give admin ability to dynamically add order items on that page


admin.site.register(Order, OrderAdmin)
admin.site.register(User)
admin.site.register(Product)