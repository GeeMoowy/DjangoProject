from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator

from catalog.models import Product
from .forms import ProductForm


def home(request):
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'home.html', {'products': products})


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо {name}! Ваши данный приняты.")
    return render(request, 'contacts.html')


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)  # Получаем продукт по ID
    return render(request, 'product_detail.html', {'product': product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm
    return render(request, 'add_product.html', {'form': form})
