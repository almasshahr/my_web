from django.test import TestCase
from django.shortcuts import reverse

from .models import pages


class pagesTest(TestCase):
    def setUp(self):
       self.page = pages.objects.create(title='ho', text='text', auther='jack')

    def test_pageView(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_NamePage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_contentPage(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response,self.page.text)

