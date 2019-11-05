from django.contrib import admin 
from .models import Item, OrderItem, Order, Payment, Coupon, Refund
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display =[
                'user', 
                'ordered',
                'received',
                'refund_requested',
                'refund_granted',
                'user',
                'billing_address',
                'payment',
                'coupon',
                ]

    list_display_links = [
                'user',
                'billing_address',
                'payment',
                'coupon',
                    ]

    list_filter = [
                'user', 
                'ordered',
                'received',
                'refund_requested',
                'refund_granted'
                ]

    search_fields = [
        'user__username',
        'ref_code'
    ]

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order,  OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)