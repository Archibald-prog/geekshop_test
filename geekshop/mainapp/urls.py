from django.urls import path
"""импортируем функцию products из модуля mainapp/views.py"""
from .views import products, product

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='main'),
    path('category/<int:pk>', products, name='category'),
    path('product/<int:pk>', product, name='detail'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
]

