from django.core.cache import cache
from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст записывает данные в кэш"""
    if not CACHE_ENABLED:
        return Product.objects.filter(is_published=True)
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(is_published=True)
    cache.set(key, products)
    return products


def get_products_by_category(category_id):
    """Возвращает список всех продуктов в указанной категории."""
    return Product.objects.filter(category_id=category_id, is_published=True)
