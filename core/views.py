from django.shortcuts import render
from category.models import Category
from store.models import Product
from django.db.models import Q

def home(request):
    bannerCategories = Category.objects.all()[0:8]
    babies = Product.objects.filter(category__name = "Toys")[0:5]
    beauty = Product.objects.filter(category__name = "Health & Personal Care")[0:5]
    books = Product.objects.filter(category__name = "Books")[0:5]
    electronics = Product.objects.filter(category__name = "Electronics")[0:5]
    categories1 = Category.objects.all()[8:16]
    context = {
        'bannerCategories': bannerCategories,
        'babies': babies,
        'beauty':beauty,
        'categories1': categories1,
        'books': books,
        'electronics':electronics,
    }
    return render(request, 'home.html', context)