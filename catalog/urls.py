from django.urls import path
from catalog.apps import CatalogConfig
from .views import contacts, product_detail, add_product, HomeView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('add_product/', add_product, name='add_product')
]