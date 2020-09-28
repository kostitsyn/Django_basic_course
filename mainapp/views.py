from django.shortcuts import render

from mainapp.models import Games, LocationGame

name_game = [
    {'href': 'battlefield_1', 'name': 'BATTLEFIELD 1', 'img': 'battlefield_1.jpg'},
    {'href': 'star_wars', 'name': 'STAR WARS: Battlefront II', 'img': 'battlefront_1.jpg'},
    {'href': 'battlefield_4', 'name': 'BATTLEFIELD 4', 'img': 'battlefield_4.jpg'},
    {'href': 'world_of_tanks', 'name': 'WORLD OF TANKS', 'img': 'tanks.jpg'},
    {'href': 'assasin', 'name': 'ASASSIN’S CREED: Rogue', 'img': 'asassin.jpg'},
    {'href': 'for_honor', 'name': 'FOR HONOR', 'img': 'honor.jpg'},
    {'href': 'world_of_warships', 'name': 'WORLD OF WARSHIPS', 'img': 'warships.jpg'},
    {'href': 'call_of_duty', 'name': 'CALL OF DUTY: Infinite Warface', 'img': 'call-of-duty.jpg'},
]

def main(request, pk=None):
    game_list = Games.objects.filter(site_location=1)
    content = {
        'name_page': 'historical games',
        'css_file': 'style-index.css',
        'games': game_list
    }
    return render(request, 'mainapp/index.html', content)

def gallery(request, pk=None):
    game_list = Games.objects.filter(site_location=2)
    game_discount = Games.objects.filter(site_location=3)
    content = {
        'name_page': 'gallery',
        'css_file': 'style-gallery.css',
        'games': game_list,
        'games_discount': game_discount,
    }
    return render(request, 'mainapp/gallery.html', content)

def contacts(request):
    content = {
        'name_page': 'contacts',
        'css_file': 'style-product-page.css'
    }
    return render(request, 'mainapp/contacts.html', content)

def assasin(request):
    content = {
        'name_page': 'assasin game',
        'css_file': 'style-product-page.css'
    }
    return render(request, 'mainapp/assasin.html', content)
