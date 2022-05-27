from django.shortcuts import redirect, render,get_object_or_404
from .models import Product
from django.contrib.auth.models import User

# Create your views here.

def homepage(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products':products})

def detail(request,product_id):
    product = get_object_or_404(Product, pk = product_id)
    return render(request, 'detail.html', {'product':product})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_product = Product()
    new_product.writer = request.user
    new_product.name = request.POST['name']
    new_product.discription = request.POST['discription']
    new_product.keyword = request.POST['keyword']
    new_product.image = request.FILES['image']
    new_product.save()
    return redirect('detail', new_product.id)

def edit(request, product_id):
    edit_product = Product.objects.get(pk = product_id)
    return render(request, 'edit.html', {'product':edit_product})

def update(request,product_id):
    update_product = Product.objects.get(pk=product_id)
    update_product.writer = request.user
    update_product.name = request.POST['name']
    update_product.discription = request.POST['discription']
    update_product.keyword = request.POST['keyword']
    if request.FILES.get("image"):
        update_product.image = request.FILES['image']
    update_product.save()
    return redirect('detail', update_product.id)

def delete(request, product_id):
    delete_product = Product.objects.get(pk=product_id)
    delete_product.delete()
    return redirect('homepage')

def onsale(request, product_id):
    product = Product.objects.get(pk = product_id)
    if product.onSale is True:
        product.onSale = False
        product.save()
    else:
        product.onSale = True
        product.save()
    return redirect('detail', product_id)


def follow(request, product_id, user_id):
    user = request.user
    followed_user = get_object_or_404(User, pk=user_id)
    is_follower = user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('detail', product_id)

def followingProduct(request):
    user = request.user
    followings = user.profile.followings.all()
    productList = []
    for following in followings:
        products = Product.objects.filter(writer = following.user)
        list_of_product = products[::1]
        productList.append(list_of_product)
    productLists = sum(productList, [])
    return render(request, 'followingProduct.html', {'products':productLists})