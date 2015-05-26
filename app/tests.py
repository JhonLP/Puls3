from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Categoria, Enlace
from django.contrib.auth.models import User

class SimpleTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(titulo='Categoria de prueba')
        self.usuario = User.objects.create_user(username='julian', password='barbas')

    def test_views(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(reverse('about'))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(reverse('enlaces'))
        self.assertEqual(res.status_code, 200)

        self.assertTrue(self.client.login(username='julian', password='barbas'))

        res = self.client.get(reverse('add'))
        self.assertEqual(res.status_code, 200)

    def test_add(self):
        self.assertTrue(self.client.login(username='julian', password='barbas'))
        self.assertEqual(Enlace.objects.count(), 0)
        data = {}
        data['titulo'] = 'Test titulo'
        data['enlace'] = 'http://mejorando.la/'
        data['categoria'] = self.categoria.id
        res = self.client.post(reverse('add'), data)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Enlace.objects.count(), 1)

        enlace = Enlace.objects.all()[0]
        self.assertEqual(enlace.titulo, data['titulo'])
        self.assertEqual(enlace.enlace, data['enlace'])
        self.assertEqual(enlace.categoria, self.categoria)