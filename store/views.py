from django.shortcuts import render, get_object_or_404
from category.models import Category
from store.models import Product

def store(request, category_slug=None):
    categ = None
    products = None
    if category_slug != None:
        categ = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categ, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all()
        product_count = products.count()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise e
    related_products = Product.objects.filter(category=single_product.category, is_available=True)
    most_bought_products = Product.objects.filter(is_available=True)[0:5]
    context = {'single_product': single_product, "related_products":related_products, "most_bought_products":most_bought_products}
    return render(request, 'store/product_detail.html', context)
