from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from random import randint

def home_page(request):
    context = {
        'name': 'Stanley',
        'pic1': 'https://picsum.photos/200/300/?image=100',
        'pic2': 'https://picsum.photos/200/300/?image=101',
        'pic3': 'https://picsum.photos/200/300/?image=102'
        }
    response = render(request, 'index.html', context)
    return response

def portfolio(request):
    random_num = randint(0,100)

    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))
    context = {
        'gallery_image': image_urls
    }
    response = render(request, 'gallery.html', context)
    return response

def about_me(request):
    skills = ['HTML', 'Python', 'Django']
    interest = ['Archery', 'Fire Emblem', 'TFT']
    context = {'skills': skills, 'interests': interest}
    response = render(request, 'about.html', context)
    return response

def favorites(request):
    fav_sites = ['https://roosterteeth.com/', 'https://www.youtube.com/', 'https://www.reddit.com/']
    context = {'fav_sites': fav_sites}
    response = render(request, 'fav.html', context)
    return response

def root(request):
    return HttpResponseRedirect('/home')

def gallery(request):
    return HttpResponseRedirect('/portfolio')