from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from .import views
# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('katalog:index')
        self.assertEquals(resolve(url).func, views.index)

class TestViews(TestCase):
    def test_katalog_list_GET(self):
        client = Client()
        response = client.get(reverse('katalog:index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')