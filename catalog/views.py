from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView, View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from catalog.models import Product
from .forms import ProductForm, ContactsForm


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_moderator'] = self.request.user.groups.filter(name='Модератор продуктов').exists()
        return context


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


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user:
            return HttpResponseForbidden("У Вас нет прав для редактирования этого продукта.")
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
    context_object_name = 'product'

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        if product.owner == request.user:
            return super().dispatch(request, *args, **kwargs)

        if request.user.groups.filter(name='Модератор продуктов').exists():
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseForbidden("У Вас нет прав для удаления этого продукта.")


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.Can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('catalog.Can_unpublish_product'):
            return HttpResponseForbidden('Нужны права модератора продуктов')

        product.is_published = False
        product.save()
        return redirect('catalog:home')
