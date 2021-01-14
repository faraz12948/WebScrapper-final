import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models
from django.http import JsonResponse
import json







base_url='https://www.techlandbd.com/index.php?route=product/search&search={}'

# Create your views here.
def home(request):
    return render(request, 'base1.html')


def new_search1(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    s=quote_plus(search)


    final_url = base_url.format(s)


    result = requests.get(final_url)
    src = result.content
    soup = BeautifulSoup( src , 'lxml')


    product_list =soup.find_all("div",{"class" : "product-thumb"})


    product_info = []

    for product in product_list:
        product_title = product.find(class_='name').text
        product_url = product.find('a',href=True).get('href')
    
    

        if product.find(class_='normal-price'):
              product_price = product.find(class_='normal-price').text
            
        else:
              product_price = 'N/A'

        if product.find(class_='image'):
              product_image_url = product.find('img').get('src')
       

        product_info.append((product_title, product_url, product_price,product_image_url))


    
    #jason_format = jason.dumps(jason_dict)
    #print(jason_format)


    stuff_for_frontend = {
            'search': search,
            'final_postings': product_info,
        }

    return render(request, 'my_app/new_search1.html', stuff_for_frontend)
    #return JsonResponse(stuff_for_frontend)


