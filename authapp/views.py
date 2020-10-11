from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def login(request):
    css_file = ['style-index.css', 'bootstrap.min.css']

    next_url = request.GET.get('next', '')

    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main'))

    content = {'name_page': 'вход', 'login_form': login_form, 'css_file': css_file, 'next': next_url}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    css_file = ['style-index.css', 'bootstrap.min.css']

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = ShopUserRegisterForm()
    content = {'name_page': 'регистрация', 'register_form': register_form, 'css_file': css_file}
    return render(request, 'authapp/register.html', content)


def edit(request):
    css_file = ['style-index.css', 'bootstrap.min.css']
    if request.method == "POST":
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))

    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {'name_page': 'редактирование', 'edit_form': edit_form, 'css_file': css_file}

    return render(request, 'authapp/edit.html', content)