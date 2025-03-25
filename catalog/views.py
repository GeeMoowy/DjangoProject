from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]

    for product in latest_products:
        print(f'Продукт: {product.name}, Цена: {product.purchase_price}, Дата создания: {product.created_at}')

    return render(request, 'home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо {name}! Ваши данный приняты.")
    return render(request, 'contacts.html')
