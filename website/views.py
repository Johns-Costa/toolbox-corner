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

def welcome(request):
    """Render the welcome page."""
    return render(request, 'website/welcome.html')

def home(request):
    """
    Display the home page with all products and their first images.
    Also calculates the average rating for each product.
    """
    products = Product.objects.all()
    product_images = {}
    categories = Category.objects.all()

    for product in products:
        # Fetch the first image for each product
        first_image = product.images.first()
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
    """
    Display products filtered by a specific category, their images, and average ratings.
    """
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    product_images = {}
    
    for product in products:
        # Fetch the first image for each product
        first_image = product.images.first()
        product_images[product.id] = first_image
        
        # Calculate average rating for the product
        average_rating = Review.objects.filter(product=product).aggregate(Avg('stars'))['stars__avg']
        setattr(product, 'average_rating', average_rating if average_rating else "No reviews")

    context = {
        'category': category,
        'products': products,
        'product_images': product_images,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'website/category_products.html', context)

def product_detail(request, product_id):
    """
    Display detailed information about a specific product, including images and average ratings.
    """
    product = get_object_or_404(Product, pk=product_id)
    
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
    """
    Display products matching the search query, their images, and average ratings.
    """
    query = request.GET.get('q')
    results = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query)
    product_images = {}
    
    for product in results:
        # Fetch the first image for each product
        first_image = product.images.first()
        product_images[product.id] = first_image
        
        # Calculate average rating for the product
        average_rating = Review.objects.filter(product=product).aggregate(Avg('stars'))['stars__avg']
        setattr(product, 'average_rating', average_rating if average_rating else "No reviews")

    context = {
        'query': query,
        'results': results,
        'product_images': product_images,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'website/search_results.html', context)

@staff_member_required
def add_product(request):
    """
    Allows staff members to add new products and upload images.
    Handles both GET (display form) and POST (process form submission) requests.
    """
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
    """
    Allows staff members to edit existing products and manage associated images.
    Handles both GET (display form) and POST (process form submission) requests.
    """
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
    """
    Allows staff members to delete products.
    Handles both GET (display confirmation) and POST (process deletion) requests.
    """
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'website/delete_product.html', {'product': product})

@login_required
def order_product(request, product_id):
    """
    Placeholder for handling product orders.
    Requires implementation of order logic.
    """
    # Logic to handle ordering products
    return redirect('home')
