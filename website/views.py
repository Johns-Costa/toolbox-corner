from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Product, ProductImage
from .forms import ProductForm
from django.conf import settings

def home(request):
    products = Product.objects.all()
    product_images = {}
    for product in products:
        # Fetch the first image for each product
        first_image = product.images.first()
        # Add the product and its first image to the dictionary
        product_images[product.id] = first_image
    # Pass MEDIA_URL to the context
    context = {
        'products': products,
        'product_images': product_images,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'website/home.html', context)

def product_detail(request, product_id):
    # Fetch the product object
    product = get_object_or_404(Product, id=product_id)
    
    # Fetch images associated with the product
    product_images = ProductImage.objects.filter(product=product)
    
    context = {
        'product': product,
        'product_images': product_images,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    
    return render(request, 'website/product_detail.html', context)

@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            # Process and save product images
            for image in request.FILES.getlist('images'):
                product_image = ProductImage(product=product, image=image)
                product_image.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'website/add_product.html', {'form': form})

@staff_member_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'website/edit_product.html', {'form': form, 'product': product})

@staff_member_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'website/delete_product.html', {'product': product})

@login_required
def order_product(request, product_id):
    # Logic to handle ordering products
    return redirect('home')
