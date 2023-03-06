from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "created_by",
            "title",
            "slug",
            "image",
            "description",
            "category",
            "price",
            "in_stock",
            "in_active",
        )


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "title",
            "slug",
            "description",
            "category",
            "price",
            "in_stock",
            "in_active",
        )
