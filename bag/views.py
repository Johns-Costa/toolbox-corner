from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from website.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_bag(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    bag = request.session.get('bag', {})

    if str(product_id) in bag:
        bag[str(product_id)] += quantity
    else:
        bag[str(product_id)] = quantity

    if bag[str(product_id)] <= 0:
        del bag[str(product_id)]

    request.session['bag'] = bag
    messages.success(request, f'Updated {product.name} quantity in your bag')
    return redirect('view_bag')

@login_required
def view_bag(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, id=product_id)
        item_total = product.price * quantity
        total += item_total
        bag_items.append({'product': product, 'quantity': quantity, 'item_total': item_total})
    return render(request, 'bag/bag.html', {'bag_items': bag_items, 'total': total})

@login_required
def remove_from_bag(request, product_id):
    bag = request.session.get('bag', {})
    quantity = int(request.POST.get('quantity', 0))
    if str(product_id) in bag:
        if quantity == 0:
            del bag[str(product_id)]
        else:
            bag[str(product_id)] += quantity
            if bag[str(product_id)] <= 0:
                del bag[str(product_id)]

    request.session['bag'] = bag
    messages.success(request, 'Item quantity updated in your bag')
    return redirect('view_bag')
