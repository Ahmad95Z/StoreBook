from django.db import models
from django.conf import settings
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(in_active=True)


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="product_creator",default='admin'
    )
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="articles/")
    slug = models.SlugField(max_length=250, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    in_stock = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self) -> str:
        return self.title
