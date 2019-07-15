from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm


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


def product_create_view3(request):
    form = RawProductForm()

    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, "products/product_create3.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)


def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)
