from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Product, ProductImage, Category
from .forms import ProductForm, ProductImageFormSet
from django.conf import settings
from django.urls import reverse
from review.models import Review
from django.db.models import Avg


def home(request):
    products = Product.objects.all()
    product_images = {}
    categories = Category.objects.all()

    for product in products:
        # Fetch the first image for each product
        first_image = product.images.first()
        # Add the product and its first image to the dictionary
        product_images[product.id] = first_image

        # Calculate average rating for the product
        average_rating = Review.objects.filter(product=product).aggregate(Avg('stars'))['stars__avg']
        setattr(product, 'average_rating', average_rating if average_rating else "No reviews")

    context = {
        'categories': categories,
        'products': products,
        'product_images': product_images,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'website/home.html', context)

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    product_images = {product.id: product.images.first() for product in products}

    context = {
        'category': category,
        'products': products,
        'product_images': product_images,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'website/category_products.html', context)

def product_detail(request, product_id):
    # Fetch the product object
    product = get_object_or_404(Product, id=product_id)
    
    # Fetch images associated with the product
    product_images = ProductImage.objects.filter(product=product)

    # Calculate the average rating for the product
    average_rating = Review.objects.filter(product=product).aggregate(Avg('stars'))['stars__avg']
    
    context = {
        'product': product,
        'product_images': product_images,
        'MEDIA_URL': settings.MEDIA_URL,
        'average_rating': average_rating,
    }
    
    return render(request, 'website/product_detail.html', context)

def search_results(request):
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
    context = {
        'query': query,
        'results': results,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'website/search_results.html', context)

@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        image_formset = ProductImageFormSet(request.POST, request.FILES, queryset=ProductImage.objects.none(), prefix='image')
        if form.is_valid() and image_formset.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            for image_form in image_formset:
                if image_form.cleaned_data.get('image'):
                    image = image_form.cleaned_data['image']
                    ProductImage.objects.create(product=product, image=image)
            return redirect('product_detail', product.id)
    else:
        form = ProductForm()
        image_formset = ProductImageFormSet(queryset=ProductImage.objects.none(), prefix='image')
    return render(request, 'website/add_product.html', {'form': form, 'image_formset': image_formset})

@staff_member_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        image_formset = ProductImageFormSet(request.POST, request.FILES, queryset=product.images.all())

        if form.is_valid() and image_formset.is_valid():
            product = form.save()

            for form in image_formset:
                if form.cleaned_data.get('DELETE'):
                    if form.instance.pk:
                        form.instance.delete()
                elif form.cleaned_data.get('image'):
                    image_instance = form.save(commit=False)
                    image_instance.product = product
                    image_instance.save()

            messages.success(request, 'Product updated successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm(instance=product)
        image_formset = ProductImageFormSet(queryset=product.images.all())

    return render(request, 'website/edit_product.html', {
        'form': form,
        'image_formset': image_formset,
        'product': product,
    })

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
