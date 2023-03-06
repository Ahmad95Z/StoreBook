from django.urls import path
from . import views
from .views import *

app_name = "store"

urlpatterns = [
    path("", views.all_products, name="home"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("shop/<slug:category_slug>/", views.category_list, name="category_list"),
    path("add_product/", AddProduct.as_view(), name="add_product"),
     path('posts/<int:pk>/delete',DeleteProduct.as_view(), name='delete_product'),
]
