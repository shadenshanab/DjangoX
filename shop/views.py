from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Shop


class ShopListView(ListView):
    template_name = "shop/shop-list.html"
    model = Shop


class ShopDetailView(DetailView):
    template_name = "shop/shop-detail.html"
    model = Shop


class ShopCreateView(CreateView):
    template_name = "shop/shop-create.html"
    model = Shop
    fields = ['title', 'chef', 'description', 'price', 'picture']


class ShopUpdateView(UpdateView):
    template_name = "shop/shop-update.html"
    model = Shop
    fields = ['title', 'chef', 'description', 'price', 'picture']


class ShopDeleteView(DeleteView):
    template_name = "shop/shop-delete.html"
    model = Shop
    success_url = reverse_lazy("shop-list")