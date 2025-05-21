from django.http import HttpResponse
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.models import Product
from .forms import ProductForm, ContactsForm


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ContactsView(LoginRequiredMixin, FormView):
    template_name = 'contacts.html'
    form_class = ContactsForm
    success_url = reverse_lazy('catalog:contacts')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        return HttpResponse(f"Спасибо {name}! Ваши данные приняты.")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
    context_object_name = 'product'
