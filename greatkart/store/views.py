from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category

# Create your views here.

def store(request, category_slug=None):
    

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True).order_by('-created_at')

    else:

        products = Product.objects.filter(is_available=True).order_by('-created_at')

    context = {
        'products' : products,
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):

    # category = get_object_or_404(Category, slug=category_slug)
    # product = Product.objects.get(category=category, slug=product_slug, is_available=True)

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug, is_available=True)

    context = {
        'product' : product,
    }

    return render(request, 'store/product_detail.html', context)