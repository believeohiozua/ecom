from django.contrib import admin 
from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address
# Register your models here.

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)
make_refund_accepted.short_description = 'Update order to refund Granted'

class OrderAdmin(admin.ModelAdmin):
    list_display =[
                'user', 
                'ordered',
                'received',
                'refund_requested',
                'refund_granted',
                'user',
                'billing_address',
                'shipping_address',
                'payment',
                'coupon',
                ]

    list_display_links = [
                'user',
                'shipping_address',
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
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display= [
                    'user',
                    'country',
                    'street_address',
                    'apartment_address',
                    'zip',
                    'address_type',
                    'default',
                 ]

    search_fields = [
                    'user',
                    'country',
                    'street_address',
                    'apartment_address',
                    'zip',
                        ]

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order,  OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)