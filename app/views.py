from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from datetime import datetime
from models import *
from django.shortcuts import get_object_or_404
from forms import *
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from serializers import EnlaceSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page

#@cache_page(6000)
def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.order_by("-votos").all()[:50] #limita a 50 resultados
	template = "index.html"
	return render(request,template,locals())
	#locals() toma las variables definidas dentro de la funcion

def categoria(request,id_categoria):
	categorias = Categoria.objects.all()
	cat = get_object_or_404(Categoria, pk=id_categoria)
	#cat = Categoria.objects.get(pk=id_categoria)
	enlaces = Enlace.objects.filter(cat = cat)
	template = "index.html"
	return render(request,template,locals())

@login_required
def minus(request, id_enlace):
	enlace = Enlace.objects.get(pk=id_enlace)
	enlace.votos = enlace.votos - 1
	enlace.save()
	return HttpResponseRedirect("/")

@login_required
def plus(request, id_enlace):
	enlace = Enlace.objects.get(pk=id_enlace)
	enlace.votos = enlace.votos + 1
	enlace.save()
	return HttpResponseRedirect("/")

@login_required
def add(request):
	categorias = Categoria.objects.all()
	if request.method == "POST":
		form = EnlaceForm(request.POST)
		if form.is_valid():
			enlace = form.save(commit = False)
			enlace.usuario = request.user
			enlace.save()
			return HttpResponseRedirect("/")
	else:
		form = EnlaceForm()

	template = "form.html"
	return render_to_response(template, context_instance = RequestContext(request,locals()))

class EnlaceListView(ListView):
	model = Enlace
	context_object_name = 'enlaces'
	def get_template_names(self):
		return 'index.html'

class EnlaceDetailView(DetailView):
	model = Enlace
	def get_template_names(self):
		return 'index.html'

class EnlaceViewSet(viewsets.ModelViewSet):
	queryset = Enlace.objects.all()
	serializer_class = EnlaceSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

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