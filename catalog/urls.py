from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from .views import (HomeView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
                    ProductUnpublishView, ProductsByCategoryView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('<int:pk>/product_update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/product_delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/product_unpublish/', ProductUnpublishView.as_view(), name='product_unpublish'),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]