from random import choice
from django.core.urlresolvers import reverse
from django.core.cache import cache

frases = ['frase 1','frase 2','frase 3']

def ejemplo(request):
	frase = cache.get('frase_cool')
	if frase is None:
		frase = choice(frases)
		cache.set('frase_cool')
 	return {'frase':frase}

def menu(request):
	menu = {'menu':[
	{'name':'Home', 'url':reverse('home')},
	{'name':'Agregar', 'url':reverse('add')},
	{'name':'Acerca de', 'url':reverse('about')},
	]}
	for item in menu['menu']:
		if request.path == item ['url']:
			item['active'] = True
	return menu