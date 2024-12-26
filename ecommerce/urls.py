from django.urls import path

from .views import add_to_cart, get_cart, checkout, generate_discount, admin_stats

urlpatterns = [
    path('cart/<str:user_id>/', add_to_cart),
    path('cart/<str:user_id>/', get_cart),
    path('checkout/<str:user_id>/', checkout),
    path('generate_discount/', generate_discount),
    path('admin/stats/', admin_stats),
]
