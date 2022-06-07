from django.shortcuts import render

from .models import Category


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'category.html', locals())