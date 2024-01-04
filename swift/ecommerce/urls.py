from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'items', ItemViewSet)

urlpatterns = [
    path('categories/', views.CategoryViewSet.as_view(), name="categories"),
    path('items/', views.ItemViewSet.as_view(), name="items")
]