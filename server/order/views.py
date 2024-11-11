# home/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm, OrderItemForm
from .models import Order, MenuItem, Category, OrderItem, Table
from django.utils import timezone


def menu_view(request):
    categories = Category.objects.all()
    items = MenuItem.objects.all()
    tables = Table.objects.filter(is_occupied=False)
    context = {
        'categories': categories,
        'items': items,
        'tables': tables
    }
    return render(request, 'order/create_order.html', context)


# def create_order(request):
#     if request.method == 'POST':
#         order_form = OrderForm(request.POST)
#         order_item_form = OrderItemForm(request.POST)
#         if order_form.is_valid() and order_item_form.is_valid():
#             order = order_form.save()
#             order_item = order_item_form.save(commit=False)
#             order_item.order = order
#             order_item.save()
#             return redirect('order_list')  # Redirect to order list view or a success page
#     else:
#         order_form = OrderForm()
#         order_item_form = OrderItemForm()
#     return render(request, 'order/create_order.html', {
#         'order_form': order_form,
#         'order_item_form': order_item_form,
#     })

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})

from django.db.models import Case, When

def kitchen_view(request):
    
    
    # Sort by status and then by created_at (oldest orders come first)
    orders = Order.objects.prefetch_related('orderitem_set__menu_item').annotate(
        custom_order=Case(
            When(status="Pending", then=0),
            When(status="In Progress", then=1),
            When(status="Completed", then=2),
            default=3
        )
    ).order_by('custom_order', 'created_at')
    
    return render(request, 'order/kitchen_view.html', {'orders': orders})



def mark_order_complete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Completed'  # Update the status to 'Completed'
    order.save()  # Save the change to the database
    return redirect('kitchen_view')  # Redirect back to the kitchen orders view


# View to mark an order as paid
def mark_order_paid(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Update the order status to 'Paid'
    order.status = 'Paid'
    order.save()

    # Redirect back to the order list
    return redirect('order_list')

def order_review(request):
    if request.method == 'POST':
        # Get selected items and quantities
        print(f'Data: {request.POST}')
        selected_item_ids = request.POST.getlist('selected_items')
        selected_items = MenuItem.objects.filter(id__in=selected_item_ids)
        
        # Get quantities
        quantities = {
            int(item_id): int(request.POST.get(f'quantity_{item_id}', 1))
            for item_id in selected_item_ids
        }

        table = Table.objects.get(id=request.POST.get('table'))
        
        order = Order(table=table)
        order.save()
        for menu in selected_items:
            order.items.add(menu)
            
        items = OrderItem.objects.filter(order=order, menu_item__in=order.items.all())
        print(f'Item: {items}')
        
        
        return render(request, 'order/review.html', {
            'selected_items': selected_items, 
            'quantities': quantities,
            'order': order
        })
        
        
        

def submit_order(request):
    if request.method == 'POST':
        # Get special request
        special_request = request.POST.get('special_request', '')

        # Create a new order
        order = Order.objects.create(special_request=special_request, status='Pending', created_at=timezone.now())
        
        # Add items to the order
        item_ids = request.POST.getlist('items')
        for item_id in item_ids:
            quantity = int(request.POST.get(f'quantities_{item_id}', 1))
            menu_item = MenuItem.objects.get(id=item_id)
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
        
        return redirect('kitchen_view')
    return redirect('order_review')



