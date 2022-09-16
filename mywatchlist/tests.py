from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from .import views
# Create your tests here.
class TestViews(TestCase):
    def test_watchlist_html_GET(self):
        client = Client()
        response = client.get(reverse('mywatchlist:show_html'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
    
    def test_watchlist_json_GET(self):
        client = Client()
        response = client.get(reverse('mywatchlist:show_json'))

        self.assertEquals(response.status_code, 200)

    def test_watchlist_xml_GET(self):
        client = Client()
        response = client.get(reverse('mywatchlist:show_xml'))

        self.assertEquals(response.status_code, 200)