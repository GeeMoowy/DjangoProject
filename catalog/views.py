from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, FormView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from catalog.models import Product
from .forms import ProductForm, ContactsForm


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.all()


class ContactsView(FormView):
    template_name = 'contacts.html'
    form_class = ContactsForm
    success_url = reverse_lazy('catalog:contacts')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        return HttpResponse(f"Спасибо {name}! Ваши данные приняты.")


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
