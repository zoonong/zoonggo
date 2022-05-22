from itertools import product
from django.shortcuts import redirect, render,get_list_or_404
from .models import Product
# Create your views here.

def homepage(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products':products})

def detail(request,id):
    product = get_list_or_404(Product, pk = id)
    return render(request, 'detail.html', {'product':product})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_product = Product()
    new_product.writer = request.user
    new_product.name = request.post['name']
    new_product.discription = request.post['discription']
    new_product.keyword = request.post['keyword']
    new_product.image = request.FILES['image']
    new_product.save()
    return redirect('detail', new_product.id)

def edit(request, id):
    edit_product = Product.objects.get(pk = id)
    return render(request, 'edit.html', {'product':edit_product})

def update(request,id):
    update_product = Product.objects.get(pk=id)
    update_product.writer = request.user
    update_product.name = request.post['name']
    update_product.discription = request.post['discription']
    update_product.keyword = request.post['keyword']
    update_product.image = request.FILES['image']
    update_product.save()
    return redirect('detail', update_product.id)

def delete(request, id):
    delete_product = Product.objects.get(pk=id)
    delete_product.delete()
    return redirect('home')