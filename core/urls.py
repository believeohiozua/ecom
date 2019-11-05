from django.urls import path 
from django.conf.urls import url
#views
from .views import (
    homeView,
   ItemDetailView,
   add_to_cart,
   remove_from_cart,
   CheckoutView,
   OrderSummaryView,
   remove_single_item_from_cart,
   PaymentView,
   AddCouponView,
   RequestRefundView,
)
 
app_name= 'core'
urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('item/<slug>/', ItemDetailView.as_view(), name='item-detail'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single/<slug>/',  remove_single_item_from_cart, name='remove-single'),
    path('check-out/', CheckoutView.as_view(), name='check-out'),
    path('order-summary/',  OrderSummaryView.as_view(), name='order-summary'),
    path('payment/<payment_option>/',  PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
]
