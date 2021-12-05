from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Contact, Product


def main(request):
    title = 'Магазин'
    # basket = []
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)

    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:4]

    context = {
        'title': title,
        'products': products,
        # 'basket': basket,
        # 'basket_count': basket,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'Контакты'
    # basket = []
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)

    locations = Contact.objects.all()[:3]
    context = {
        'title': title,
        'locations': locations,
        # 'basket': basket,
    }
    return render(request, 'geekshop/contact.html', context)
