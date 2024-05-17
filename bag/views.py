# views.py
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from website.models import Product
from .models import BagItem
from django.contrib.auth.decorators import login_required

@login_required
def add_to_bag(request, product_id):
    product = Product.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    
    if product_id in bag:
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity
    
    request.session['bag'] = bag
    messages.success(request, f'Added {quantity} {product.name} to your bag')
    return redirect(reverse('product_detail', args=[product_id]))

@login_required
def view_bag(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    for product_id, quantity in bag.items():
        product = Product.objects.get(id=product_id)
        item_total = product.price * quantity
        total += item_total
        bag_items.append({'product': product, 'quantity': quantity, 'item_total': item_total})
    return render(request, 'bag/bag.html', {'bag_items': bag_items, 'total': total})

@login_required
def remove_from_bag(request, product_id):
    bag = request.session.get('bag', {})
    if str(product_id) in bag:
        del bag[str(product_id)]
    request.session['bag'] = bag
    messages.success(request, 'Item removed from your bag')
    return redirect('view_bag')
