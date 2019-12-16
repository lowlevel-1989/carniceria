from decimal import Decimal
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from carton.cart import Cart
from apps.product.models import Product
from apps.product.filters import ProductFilter
from apps.ticket.models import Ticket


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return ProductFilter(
                    self.request.GET,
                    queryset=super().get_queryset()
        ).qs


class ProductDetailView(DetailView):
    model = Product

class TicketDetailView(LoginRequiredMixin, DetailView):
    template_name = 'shop/ticket.html'
    model = Ticket

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class CartShowView(TemplateView):
    template_name = 'shop/cart_list.html'

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        delete = action == 'delete'
        clear = action == 'clear'

        cart = Cart(request.session)
        product = Product.objects.filter(pk=request.POST.get('product')).first()
        quantity = request.POST.get('quantity', 1)

        if delete:
            if cart.is_empty is False:
                cart.remove(product)
        elif clear:
            if cart.is_empty is False:
                cart.clear()
        else:
            cart.add(product, product.price, quantity)

        if cart.is_empty:
            return redirect('product_list')

        return super().get(request, *args, **kwargs)

