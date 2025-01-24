from django.contrib import admin
from django.urls import path, include
from inventory.views import home, ProductViewSet, VendorViewSet, SaleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('vendors', VendorViewSet)
router.register('sales', SaleViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
