from itertools import product

from django.shortcuts import render
from django.http import HttpResponse

from home.forms import CreateProductForm, UpdateProductForm
from .models import Product,Service, Student
from django.contrib.auth.decorators import login_required
# Create your views here.
#Reterive

def homepage (request):
    P=Product.objects.all()
    context={
        'products':P,
    }
    return render(request, 'home/products.html', context)


def aboutus(request):
    return HttpResponse("About")

def contactus(request):
    return HttpResponse("Contact")




 #Reterive By ID

def get_item(request,id):
    try:
        product=Product.objects.get(id=id)
    except:
        return HttpResponse("Item not found")
    context={
        'product':product
    }
    return render(request,"home/product.html",context)



#Create 
# def create_product(request):
#     if request.method=="POST":
#         name=request.POST.get("name")
#         price=request.POST.get("price")
#         description=request.POST.get("description")
#         p=Product(name=name,price=price,description=description)
#         p.save()
#         return HttpResponse("product created successfully !")
#     return render(request,"home/create.html")

@login_required

def create_product(request):
    form=CreateProductForm()
    if request.method=="POST":
        form=CreateProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Product Created successfully !")
    return render(request,"home/create.html",{'form':form})



#Update
def update_product(request,id):
    try:
        product=Product.objects.get(id=id)
    except:
        return HttpResponse("Item not found")

    form=UpdateProductForm(instance=product)
    if request.method=="POST":
        form=UpdateProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponse("Product updated successfully !")

    return render(request,"home/update.html",{'form':form})


#Delete
def delete_product(request,id):
    try:
        product=Product.objects.get(id=id)
    except:
        return HttpResponse("Item not found")
    product.delete()
    return HttpResponse("Product deleted successfully !")   
 