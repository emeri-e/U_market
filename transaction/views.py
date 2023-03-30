
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import paystack

from .models import Cart, Transaction, DeliveryAddress


class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        carts = Cart.objects.filter(user=user)
        delivery_address = DeliveryAddress.objects.filter(user=user).last()
        if delivery_address is None:
            messages.error(request, 'Please add a delivery address')
            return redirect(reverse('delivery-address-create'))
        total = sum([cart.product.price * cart.quantity for cart in carts])

        # Initialize Paystack object with API key
        paystack_secret_key = settings.PAYSTACK_SECRET_KEY
        paystack_obj = paystack.initialize(paystack_secret_key)

        # Create Paystack transaction
        email = user.email
        amount = total * 100  # Convert to kobo
        ref = paystack_obj.transaction.initialize(amount=amount, email=email)['reference']

        # Create Transaction object for each distinct seller/business
        distinct_businesses = Cart.objects.filter(user=user).values_list('product__business', flat=True).distinct()
        for business_id in distinct_businesses:
            business_carts = carts.filter(product__business=business_id)
            business_total = sum([cart.product.price * cart.quantity for cart in business_carts])
            transaction = Transaction.objects.create(
                user=user,
                business=business_id,
                amount=business_total,
                reference=ref,
                status='PENDING',
                created_at=timezone.now()
            )

        # Render checkout page with Paystack form
        context = {
            'carts': carts,
            'delivery_address': delivery_address,
            'total': total,
            'reference': ref,
            'public_key': settings.PAYSTACK_PUBLIC_KEY
        }
        return render(request, 'checkout.html', context)

    def post(self, request):
        ref = request.POST.get('reference')
        if ref:
            # Verify Paystack transaction
            paystack_secret_key = settings.PAYSTACK_SECRET_KEY
            paystack_obj = paystack.initialize(paystack_secret_key)
            transaction = paystack_obj.transaction.verify(ref)

            # Get Transaction object and update status
            transaction_obj = Transaction.objects.get(reference=ref)
            transaction_obj.status = transaction['status']
            transaction_obj.updated_at = timezone.now()
            transaction_obj.save()

            # Release funds to seller if buyer confirms receipt of products
            if transaction['status'] == 'success':
                transaction_obj.release_funds()

                # Clear user's cart and redirect to order success page
                Cart.objects.filter(user=request.user).delete()
                messages.success(request, 'Order placed successfully!')
                return redirect(reverse('order-success'))

            # Redirect to checkout page with error message
            messages.error(request, 'Transaction failed, please try again or contact support')
            return redirect(reverse('checkout'))

        # Redirect to checkout page with error message
        messages.error(request, 'Invalid request, please try again or contact support')
        return redirect(reverse('checkout'))

    @method_decorator(csrf_exempt)  # Exempt this view from CSRF protection for Paystack webhook
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
