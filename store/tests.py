from django.http import HttpRequest
from django.contrib.auth.models import User
from store.models import *
from django.test import Client, TestCase, RequestFactory

from store.views import all_products


class TestViewResponse(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        Category.objects.create(name="python", slug="python")
        User.objects.create(username="admin")
        Product.objects.create(
            category_id=1,
            title="Python",
            created_by_id=1,
            slug="Python",
            price=18,
            image="i",
        )

    def test_url_hosts(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_product_detail(self):
        response = self.client.get(reverse("store:product_detail", args=["Python"]))
        self.assertEqual(response.status_code, 200)

    def test_category_list(self):
        response = self.client.get(reverse("store:category_list", args=["python"]))
        self.assertEqual(response.status_code, 200)

    def test_home_page_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>My store</title>", html)
        self.assertTrue(html.startswith("\n<!doctype html>n"))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get("/book/java")
        response = all_products(request)
        html = response.content.decode("utf8")
        self.assertIn("<title>My store</title>", html)
        self.assertTrue(html.startswith("\n<!doctype html>\n"))
        self.assertEqual(response.status_code, 200)
