import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models
from django.http import JsonResponse
import json

# Create your views here.

base_url = 'https://www.startech.com.bd/product/search/?search={}'



    
  


def home(request):
    return render(request, 'base.html')

def new_search(request):
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
        product_title = product.find(class_='product-name').text
        product_url = product.find('a').get('href')
    
    

        if product.find(class_='price'):
              product_price = product.find(class_='price').text
            
        else:
              product_price = 'N/A'

        if product.find(class_='img-holder'):
              product_image_url = product.find('img').get('src')
       

        product_info.append((product_title, product_url, product_price,product_image_url))


    
    #jason_format = jason.dumps(jason_dict)
    #print(jason_format)


    stuff_for_frontend = {
            'search': search,
            'final_postings': product_info,
        }

    return render(request, 'my_app/new_search.html', stuff_for_frontend)
     #return JsonResponse(stuff_for_frontend)





