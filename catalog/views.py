from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product


def home(request):
    products = Product.objects.all()
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
