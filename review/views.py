from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Review
from .forms import ReviewForm
from website.models import Product
from django.db.models import Avg

@login_required
def add_review(request, product_id):
    """
    Handles the submission of a new review for a given product.
    """
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product.id)
    else:
        form = ReviewForm()
    return render(request, 'review/add_review.html', {'form': form, 'product': product})

@login_required
def edit_review(request, review_id):
    """
    Handles the editing of an existing review.
    """
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('product_detail', review.product.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review/edit_review.html', {'form': form, 'review': review})

@login_required
def delete_review(request, review_id):
    """
    Handles the deletion of an existing review.
    """
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        product_id = review.product.id
        review.delete()
        return redirect('product_detail', product_id)
    return render(request, 'review/delete_review.html', {'review': review})

def review_list(request, product_id):
    """
    Displays the list of reviews for a given product.
    """
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    average_rating = reviews.aggregate(Avg('stars'))['stars__avg']
    context = {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,
    }
    return render(request, 'review/review_list.html', context)
