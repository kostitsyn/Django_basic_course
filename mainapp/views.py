import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Games, Contacts, DiscountGames, GameCategories


def get_hot_product():
    games_list = Games.objects.all()
    return random.sample(list(games_list), 1)[0]

def get_required_obj(lst, num, max_num=0):
    my_list = []
    i = 1
    while i <= num:
        rand_num = random.randint(0, len(lst) - 1)
        my_list.append(lst.pop(rand_num))
        i += 1
        if i == max_num + 1 and max_num != 0:
            break
    return my_list

def main(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    contact_data = Contacts.objects.get(pk=1)
    game_list = list(Games.objects.all())
    result_list = get_required_obj(game_list, 4)
    content = {
        'name_page': 'historical games',
        'css_file': 'style-index.css',
        'games': result_list,
        'contact_data': contact_data,
        'basket': basket
    }
    return render(request, 'mainapp/index.html', content)

def about(request):
    pass

def service(request):
    pass



def gallery(request, pk=None):


    links_menu = GameCategories.objects.all()

    # basket = list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True))
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            games = Games.objects.all()
            category = {'name': 'все'}
        else:
            category = get_object_or_404(GameCategories, pk=pk)
            games = Games.objects.filter(game_category=category).order_by('name')

        content = {'name_page': 'gallery',
                   'css_file': 'style-gallery.css',
                   'links_menu': links_menu,
                   'category': category,
                   'games': games,
                   'basket': basket,
                   }
        return render(request, 'mainapp/games_list.html', content)

    hot_product = get_hot_product()
    game_list = list(Games.objects.all().exclude(pk=hot_product.pk))
    # result_list = get_required_obj(game_list, 8)

    game_discount = list(DiscountGames.objects.all())
    result_list_discount = get_required_obj(game_discount, 2)

    content = {
        'name_page': 'gallery',
        'css_file': 'style-gallery.css',
        'games': game_list,
        'games_discount': result_list_discount,
        'links_menu': links_menu,
        'basket': basket,
        # 'hot_product': hot_product
    }
    return render(request, 'mainapp/gallery.html', content)

def news(request):
    pass

def team(request):
    pass

def contacts(request):
    contact_data = Contacts.objects.get(pk=1)

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    content = {
        'name_page': 'contacts',
        'css_file': 'style-contacts.css',
        'contact_data': contact_data,
        'basket': basket
    }
    return render(request, 'mainapp/contacts.html', content)

# def assasin(request):
#     content = {
#         'name_page': 'assasin game',
#         'css_file': 'style-product-page.css'
#     }
#     return render(request, 'mainapp/assasin.html', content)

def product(request, pk=None):
    contact_data = Contacts.objects.get(pk=1)


    # basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True)))

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    game = Games.objects.get(name=pk)
    category = game.game_category
    similar_games_list = list(Games.objects.filter(game_category=category))
    similar_games_list.remove(game)
    result_list_similar = get_required_obj(similar_games_list, len(similar_games_list), 4)
    content = {
        'name_page': game.name,
        'game': game,
        'css_file': 'style-product-page.css',
         'games': result_list_similar,
        'contact_data': contact_data,
        'basket': basket
    }
    return render(request, 'mainapp/product.html', content)
