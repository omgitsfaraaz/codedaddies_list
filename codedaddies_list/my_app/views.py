import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup

BASE_CRAIGLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'

def home(request):
	return render(request, 'base.html')

def new_search(request):
	search = request.POST.get('search')
	print(quote_plus(search))
	final_url = BASE_CRAIGLIST_URL
	response = requests.get('https://losangeles.craigslist.org/search/?query=python%20tutor')
	data = response.text
	#print(data)
	stuff_for_frontend = {
		'search': search,
	}
	return render(request, 'my_app/new_search.html', stuff_for_frontend)