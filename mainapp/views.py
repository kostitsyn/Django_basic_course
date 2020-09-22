from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html')

def gallery(request):
    return render(request, 'mainapp/gallery.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def assasin(request):
    return render(request, 'mainapp/assasin.html')