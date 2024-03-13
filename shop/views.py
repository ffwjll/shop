from django.shortcuts import render, redirect

from shop.models import Product, Order


def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': products})


def orders(request):
    if not request.user.is_authenticated:
        return redirect('signin')

    orders_list = Order.objects.filter(user=request.user)
    return render(request, 'shop/orders.html', {'orders': orders_list})


def create_order(request, id):
    if not request.user.is_authenticated:
        return redirect('signin')

    if request.method == 'POST':
        Order.objects.create(
            user=request.user,
            product_id=id,
            count=request.POST['count'],
            delivery_address=request.POST['delivery_address'],
        )
        return redirect('orders')

    return render(request, 'shop/create_order.html', {
        'product': Product.objects.get(id=id)
    })


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/product_detail.html', {'product': product})
