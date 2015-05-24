from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from datetime import datetime
from models import *

def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.all()
	template = "index.html"
	return render_to_response(template,locals())
	#locals() toma las variables definidas dentro de la funcion

def hora_actual(request):
	now = datetime.now()
	return render_to_response('hora.html', {'hora':now})
	"""
	---forma larga---
	ahora = datetime.now()
	t = get_template('hora.html')
	c = Context({'hora':ahora})
	html = t.render(c)
	return HttpResponse(html)
	"""