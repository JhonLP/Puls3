from django.contrib import admin
from models import Enlace,Categoria,Agregador
from actions import export_as_csv

class EnlaceAdmin(admin.ModelAdmin):
	list_display = ('titulo','enlace','cat','imagen_voto','es_popular','imagen',)
	list_filter = ('cat','usuario')
	search_fields = ('cat__titulo','usuario__email')
	list_editable = ('titulo','enlace','cat')
	list_display_links = ('es_popular',)
	actions = [export_as_csv]
	raw_id_fields = ('usuario',)

	def imagen_voto(self,obj):
		url = obj.mis_votos_en_imagen()
		tag = '<img src="%s"' %url
		return tag
	imagen_voto.allow_tags = True
	imagen_voto.admin_order_field = 'votos'

class EnlaceInline(admin.StackedInline):
	model = Enlace
	extra = 1
	raw_id_fields = ('usuario',)

class CategoriaAdmin(admin.ModelAdmin):
	inlines = [EnlaceInline]

class AgregadorAdmin(admin.ModelAdmin):
	filter_horizontal = ('enlaces',)

# Register your models here.
admin.site.register(Agregador, AgregadorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Enlace,EnlaceAdmin)