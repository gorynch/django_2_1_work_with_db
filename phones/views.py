import csv
from pprint import pprint

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from main.settings import CSV_PATH
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    content = Phone.objects.all()
    sort = request.GET.get('sort', '')
    if sort == 'name':
        content = list(Phone.objects.all().order_by('name').values())
    elif sort == 'min_price':
        content = list(Phone.objects.all().order_by('price').values())
    elif sort == 'max_price':
        content = list(Phone.objects.all().order_by('-price').values())
    page_number = int(request.GET.get("page", 1))
    # paginator = Paginator(list(content), 10)
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)
    context = {
        'phones': page,
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)
