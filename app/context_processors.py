from random import choice
from django.core.urlresolvers import reverse

frases = ['frase 1','frase 2','frase 3']

def ejemplo(request):
 	return {'frase':choice(frases)}

def menu(request):
	menu = {'menu':[
	{'name':'Home', 'url':reverse('home')},
	{'name':'Agregar', 'url':reverse('add')},
	]}
	for item in menu['menu']:
		if request.path == item ['url']:
			item['active'] = True
	return menu