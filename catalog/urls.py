from django.urls import path
from catalog.apps import CatalogConfig
from .views import HomeView, ContactsView, ProductDetailView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_product/', ProductCreateView.as_view(), name='add_product')
]