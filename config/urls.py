from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from product.views import toggle_like
from product.views import ProductViewSet

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title='Fullstack_hakaton',
        default_version='v1',
        description='My API'
    ),
    public=True
)
router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api/v1/', include('myaccount.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/products/<int:id>/toggle_like/', toggle_like),
]
