from django.shortcuts import redirect

def de_donde_vengo(request):
	return 'Colombia'

class PaisMiddleware():
	def process_request(self,request):
		pais = de_donde_vengo(request)
		if pais == 'Mexico':
			return redirect('http://mejorando.la')