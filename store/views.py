from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import *
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .forms import AddProductForm, UpdateProductForm
from django.db.models import Q

def all_products(request):
    products = Product.products.all()
    return render(request, "store/home.html", {"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, "store/product_detail.html", {"product": product})

    
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(
        request, "store/category.html", {"category": category, "products": products}
    )


class AddProduct(CreateView):
    model = Product
    form_class = AddProductForm
    template_name = "store/add_product.html"
    success_url = reverse_lazy("store:home")
    

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'store/delete.html'
    success_url = reverse_lazy('store:home')


class UpdateProduct(UpdateView):
    model = Product
    form_class = UpdateProductForm
    template_name = 'store/update_product.html'
    success_url = reverse_lazy('store:home')



class SearchResults(ListView):
    model = Product
    template_name = 'store/search.html'
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
    
