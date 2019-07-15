from django.shortcuts import render
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_create_view2(request):
    if request.method == 'POST':
        new_title = request.POST['title']
        print(new_title)
    context = {}
    return render(request, "products/product_create2.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
