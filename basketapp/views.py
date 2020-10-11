from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Games

@login_required
def basket(request):
    pass

@login_required
def basket_add(request, pk):
    product_item = get_object_or_404(Games, pk=pk)

    basket_item = Basket.objects.filter(product=product_item, user=request.user).first()

    if not basket_item:
        basket_item = Basket.objects.create(product=product_item, user=request.user)

    basket_item.quantity += 1
    basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, pk):
    pass
