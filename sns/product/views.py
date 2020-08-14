from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Product


class ProductCreateView(CreateView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
