import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models

BASE_CRAIGLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'

def home(request):
	return render(request, 'base.html')

def new_search(request):
	search = request.POST.get('search')
	models.Search.objects.create(search=search)
	#print(quote_plus(search))
	final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
	print(final_url)
	response = requests.get(final_url)
	data = response.text
	#print(data)
	stuff_for_frontend = {
		'search': search,
	}
	return render(request, 'my_app/new_search.html', stuff_for_frontend)