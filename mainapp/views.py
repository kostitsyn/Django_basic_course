import random

from django.shortcuts import render

from mainapp.models import Games, Contacts, DiscountGames


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
    game_list = list(Games.objects.all())
    result_list = get_required_obj(game_list, 4)
    content = {
        'name_page': 'historical games',
        'css_file': 'style-index.css',
        'games': result_list
    }
    return render(request, 'mainapp/index.html', content)

def about(request):
    pass

def service(request):
    pass



def gallery(request, pk=None):
    game_list = list(Games.objects.all())
    result_list = get_required_obj(game_list, 8)

    game_discount = list(DiscountGames.objects.all())
    result_list_discount = get_required_obj(game_discount, 2)

    content = {
        'name_page': 'gallery',
        'css_file': 'style-gallery.css',
        'games': result_list,
        'games_discount': result_list_discount,
    }
    return render(request, 'mainapp/gallery.html', content)

def news(request):
    pass

def team(request):
    pass

def contacts(request):
    contact_data = Contacts.objects.get(pk=1)
    content = {
        'name_page': 'contacts',
        'css_file': 'style-product-page.css',
        'contact_data': contact_data
    }
    return render(request, 'mainapp/contacts.html', content)

def assasin(request):
    content = {
        'name_page': 'assasin game',
        'css_file': 'style-product-page.css'
    }
    return render(request, 'mainapp/assasin.html', content)

def product(request, pk=None):
    game = Games.objects.get(name=pk)
    category = game.game_category
    similar_games_list = list(Games.objects.filter(game_category=category))
    similar_games_list.remove(game)
    result_list_similar = get_required_obj(similar_games_list, len(similar_games_list), 4)
    content = {
        'name_page': game.name,
        'game': game,
        'css_file': 'style-product-page.css',
        'similar_games': result_list_similar
    }
    return render(request, 'mainapp/product.html', content)
