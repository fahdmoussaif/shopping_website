from django.urls import path, include

from ecommerce.store import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),  # Include other app URLs here
    path('', include('ecommerce.urls')),   # Include the ecommerce app's URLs
]
