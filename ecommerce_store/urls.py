from django.contrib import admin
from django.urls import path, include
from ecommerce.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),  # This line serves the index.html at the root URL.
    path('api/', include('ecommerce.urls')),
]
