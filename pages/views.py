from django.shortcuts import render
from pages.models import *


def home_page_view(request):
    cat = request.GET.get('cat')
    sort = request.GET.get('sort')

    products = ProductModel.objects.all().order_by('-pk')
    categories = CategoryModel.objects.all().order_by('-pk')
    galleries = GalleryModel.objects.all().order_by('-pk')
    news = NewsModel.objects.all().order_by('-pk')[:3]

    if cat:
        products = products.filter(categories=cat)

    if sort:
        if sort == "-price":
            products = products.order_by('-price')
        elif sort == "price":
            products = products.order_by('price')

    context = {
        "products": products,
        "categories": categories,
        "galleries": galleries,
        "news": news
    }
    return render(request, 'index.html', context=context)


def about_page_view(request):
    workers = WorkerModel.objects.all()
    context = {
        "workers": workers,
    }
    return render(request, 'about-us.html', context=context)


def blog_page_view(request):
    news = NewsModel.objects.all()
    context = {
        "news": news
    }
    return render(request, 'blog.html', context=context)
