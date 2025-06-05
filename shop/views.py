from django.shortcuts import render, get_object_or_404
from .models import Product
from django.shortcuts import get_object_or_404,redirect 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart
from django.contrib.auth.decorators import login_required
from .models import Cart
from django.shortcuts import render
from .models import RefurbishedProduct
from django.shortcuts import redirect
from .models import Product, RefurbishedProduct, Cart
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@login_required
def add_to_cart(request, model, product_id):
    if model == "refurbished":
        model_class = RefurbishedProduct
    else:
        model_class = Product

    product = get_object_or_404(model_class, id=product_id)
    content_type = ContentType.objects.get_for_model(model_class)

    cart_item = Cart.objects.filter(
        user=request.user,
        content_type=content_type,
        object_id=product.id
    ).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        Cart.objects.create(
            user=request.user,
            content_type=content_type,
            object_id=product.id,
            quantity=1
        )

    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    # Only include items with a valid id and product
    cart_items = [item for item in cart_items if item.id and item.product]
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(Cart, id=item_id, user=request.user)
    item.delete()
    return redirect('view_cart')








def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def checkout(request):
    return render(request, 'checkout.html')


def refurbished_products(request):
    products = RefurbishedProduct.objects.all()
    return render(request, 'refurbished.html', {'products': products})



@login_required
def update_cart(request, item_id):
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('view_cart')



@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    total = 0
    for item in cart_items:
        total += item.quantity * item.product.price

    if request.method == 'POST':
        # Simulate order success
        messages.success(request, "Payment successful! Order placed.")
        Cart.objects.filter(user=request.user).delete()  # clear cart
        return redirect('home')  # change to your home page name

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total,
    })



@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        # Optional: validate fields here
        messages.success(request, "Payment successful! Thank you for your purchase.")
        return redirect('thank_you')  # Change this if needed
    return render (request,'checkout.html')


# ...existing code...

def thank_you(request):
    return render(request, 'thank_you.html')
# ...existing code...