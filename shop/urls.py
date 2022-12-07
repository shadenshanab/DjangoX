from django.urls import path
from .views import ShopListView, ShopDetailView, ShopCreateView, ShopUpdateView, ShopDeleteView

urlpatterns = [
    path('shop/', ShopListView.as_view(), name='shop-list'),
    path('shop/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
    path('shop/create/',ShopCreateView.as_view(), name='shop-create'),
    path('shop/<int:pk>/update/', ShopUpdateView.as_view(), name='shop-update'),
    path('shop/<int:pk>/delete/', ShopDeleteView.as_view(), name='shop-delete'),
]