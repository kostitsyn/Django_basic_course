from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, GameEditForm, GameReadForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import GameCategories, Games


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    css_file = ['style-index.css', 'bootstrap.min.css']
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {
        'name_page': 'пользователи/создание',
        'update_form': user_form,
        'css_file': css_file
    }

    return render(request, 'adminapp/user_update.html', content)



@user_passes_test(lambda u: u.is_superuser)
def users(request):
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    content = {
        'name_page': 'админка/пользователи',
        'objects': users_list,
    }
    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        user_form = ShopUserAdminEditForm(instance=edit_user)
    css_file = ['style-index.css', 'bootstrap.min.css']
    content = {
        'name_page': 'пользователи/редактирование',
        'update_form': user_form,
        'css_file': css_file
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST' and edit_user.is_active:
        edit_user.is_active = False
        edit_user.save()
        return HttpResponseRedirect(reverse('admin:users'))
    else:
        if edit_user.is_active == False:
            edit_user.is_active = True
            edit_user.save()
            return HttpResponseRedirect(reverse('admin:users'))



    content = {'name_page': 'пользователи/удаление',
               'user_to_delete': edit_user
               }
    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    css_file = ['style-index.css', 'bootstrap.min.css']
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        category_form = ProductCategoryEditForm()
    content = {
        'name_page': 'категории/создание',
        'update_form': category_form,
        'css_file': css_file
    }
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    categories_list = GameCategories.objects.all()
    a = request
    content = {
        'name_page': 'админка/категории',
        'objects': categories_list,
    }
    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    css_file = ['style-index.css', 'bootstrap.min.css']

    category_item = get_object_or_404(GameCategories, pk=pk)
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category_item)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:category_update', args=[category_item.pk]))
    else:
        category_form = ProductCategoryEditForm(instance=category_item)
    content = {
        'name_page': 'категории/редактирование',
        'update_form': category_form,
        'css_file': css_file
    }
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    category_item = get_object_or_404(GameCategories, pk=pk)
    products_of_category = Games.objects.filter(game_category=category_item.pk)

    if request.method == 'POST' and category_item.is_active:
        category_item.is_active = False
        category_item.save()
        for item in products_of_category:
            item.is_active = False
            item.save()
        return HttpResponseRedirect(reverse('admin:categories'))
    else:
        if category_item.is_active == False:
            category_item.is_active = True
            category_item.save()
            for item in products_of_category:
                item.is_active = True
                item.save()
            return HttpResponseRedirect(reverse('admin:categories'))



    content = {'name_page': 'категории/удаление',
               'category_to_delete': category_item
               }
    return render(request, 'adminapp/category_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    css_file = ['style-index.css', 'bootstrap.min.css']
    category_item = GameCategories.objects.get(pk=pk)

    if request.method == 'POST':
        product_form = GameReadForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        product_form = ProductCategoryEditForm()
    content = {
        'name_page': 'продукты/создание',
        'update_form': product_form,
        'css_file': css_file,
        'category': category_item,
    }
    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    category_item = get_object_or_404(GameCategories, pk=pk)
    products_list = Games.objects.filter(game_category=category_item)
    content = {
        'name_page': 'категории/игры',
        'objects': products_list,
        'category': category_item,
    }

    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    css_file = ['style-index.css', 'bootstrap.min.css']
    product_item = get_object_or_404(Games, pk=pk)
    category_item = GameCategories.objects.get(name=product_item.game_category)


    content = {
        'name_page': 'админка/игра',
        'objects': product_item,
        'category': category_item,
        'css_file': css_file,
    }

    return render(request, 'adminapp/product.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    css_file = ['style-index.css', 'bootstrap.min.css']

    product_item = get_object_or_404(Games, pk=pk)
    category_item = GameCategories.objects.get(name=product_item.game_category)

    if request.method == 'POST':
        product_form = GameEditForm(request.POST, request.FILES, instance=product_item)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[product_item.pk]))
    else:
        product_form = GameEditForm(instance=product_item)
    content = {
        'name_page': 'игры/редактирование',
        'update_form': product_form,
        'css_file': css_file,
        'category': category_item,
    }
    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    product_item = get_object_or_404(Games, pk=pk)
    category_item = GameCategories.objects.get(name=product_item.game_category)

    if request.method == 'POST' and product_item.is_active:
        product_item.is_active = False
        product_item.save()
        return HttpResponseRedirect(reverse('admin:products', args=[category_item.pk]))
    else:
        if product_item.is_active == False:
            product_item.is_active = True
            product_item.save()
            return HttpResponseRedirect(reverse('admin:products', args=[category_item.pk]))


    content = {'name_page': 'игры/удаление',
               'product_to_delete': product_item,
               'category': category_item,
               }
    return render(request, 'adminapp/product_delete.html', content)