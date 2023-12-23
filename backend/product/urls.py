from django.urls import path, include
from .views import product_index, product_detail, product_list, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', ProductViewSet, basename="items")

urlpatterns = [
    path('', include(router.urls)),
    path('all/', product_list, name="product_list"),
    path('single/<int:pk>/', product_detail, name="product_detail"),
    # path('')
]