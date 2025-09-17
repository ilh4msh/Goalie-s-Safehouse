from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm  
from main.models import Product
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    products = Product.objects.all()
    
    context = {
        "app_name": "Goalie’s Safehouse",  # nama aplikasi
        "name": "Ilham Shahputra Hasim",
        "npm": "2406401193",
        "class": "PBP A",
        "product_list": products,
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None) 

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)


def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()
    
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "show_product.html", context)

    
def show_xml(request):
    products = Product.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products = Product.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    product = Product.objects.filter(pk=product_id)
    if not product.exists():
        return HttpResponse(status=404)
    xml_data = serializers.serialize("xml", product)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, product_id):
    product = Product.objects.filter(pk=product_id)
    if not product.exists():
        return HttpResponse(status=404)
    json_data = serializers.serialize("json", product)
    return HttpResponse(json_data, content_type="application/json")    