from django.db.utils import IntegrityError
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render , redirect
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
from django.views.generic import ListView, DetailView, CreateView,UpdateView
from .models import Business, Product, Cart, Favorites, Service, ServiceBusiness, Rating
from django.contrib import messages
from django.db.models import Q
from .forms import BuzUpdateForm, ProductUpdateForm, ServiceBuzUpdateForm, ServiceUpdateForm

class BUzListView(ListView):
    model=Business
    template_name = "business/Buz_list.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business_list']= Business.objects.all()
        context['service_business_list']= ServiceBusiness.objects.all()
        return context


class BUzDetailView(DetailView):
    model = Business
    template_name = "business/Buz_detail.html"

    def get(self, request, *args, **kwargs):
        business_uuid = self.kwargs.get('pk')
        business = get_object_or_404(Business, id=business_uuid)
        context = {'business':business}
        return render(request, self.template_name, context)

class BuzCreateView(CreateView):
    model = Business
    template_name = "business/Buz_create.html"
    fields=["name",'description', 'category', 'location','ProfilePix']

    def form_valid(self, form): 
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BuzUpdateView(UpdateView):
    model = Business
    template_name = "business/Buz_update.html"
    form_class = BuzUpdateForm
    success_url = reverse_lazy('Buz_detail')

    def get_success_url(self):
        return reverse_lazy('Buz_detail', kwargs={'pk': self.object.id})

    def get_object(self, queryset=None):
        return Business.objects.get(id=self.kwargs.get('pk'))

class ServiceBuzCreateView(CreateView):
    model = ServiceBusiness
    template_name = "business/ServiceBuz_create.html"
    fields=["name",'description', 'location','ProfilePix']

    def form_valid(self, form): 
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ServiceBuzUpdateView(UpdateView):
    model = ServiceBusiness
    template_name = "business/ServiceBuz_update.html"
    form_class = ServiceBuzUpdateForm
    success_url = reverse_lazy('ServiceBuz_detail')

    def get_success_url(self):
        return reverse_lazy('ServiceBuz_detail', kwargs={'pk': self.object.id})

    def get_object(self, queryset=None):
        return ServiceBusiness.objects.get(id=self.kwargs.get('pk'))

class ServiceBUzDetailView(DetailView):
    model = ServiceBusiness
    template_name = "business/ServiceBuz_detail.html"

    def get(self, request, *args, **kwargs):
        business_uuid = self.kwargs.get('pk')
        business = get_object_or_404(ServiceBusiness, id=business_uuid)
        context = {'business':business}
        return render(request, self.template_name, context)

class ProductListView(ListView):
    model = Product
    context_object_name= "products"
    template_name = "business/product_list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "business/product_detail.html"


    def get(self, request, *args, **kwargs):
        product_uuid = self.kwargs.get('pk')
        product = get_object_or_404(Product, id=product_uuid)
        context = {'product':product, 'range':range(1,6)}
        return render(request, self.template_name, context)


class ProductCreateView(CreateView):
    model = Product
    template_name = "business/product_create.html"
    fields=["name",'description', 'category', 'price','photo', 'product_count']

    def form_valid(self, form): 
        form.instance.business = Business.objects.get(id=self.kwargs['pk'])
        if form.instance.business.owner != self.request.user:
            return HttpResponseForbidden()
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "business/product_update.html"
    form_class = ProductUpdateForm
    success_url = reverse_lazy('product_detail')

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.id})

    def get_object(self, queryset=None):
        return Product.objects.get(id=self.kwargs.get('pk'))




class ServiceListView(ListView):
    model = Service
    context_object_name= "services"
    template_name = "business/service_list.html"

class ServiceDetailView(DetailView):
    model = Service
    template_name = "business/service_detail.html"


    def get(self, request, *args, **kwargs):
        service_uuid = self.kwargs.get('pk')
        service = get_object_or_404(Service, id=service_uuid)
        context = {'service':service,'range': range(1,6)}
        return render(request, self.template_name, context)


class ServiceCreateView(CreateView):
    model = Service
    template_name = "business/service_create.html"
    fields=["name",'description', 'category', 'price','photo']

    def form_valid(self, form): 
        form.instance.business = ServiceBusiness.objects.get(id=self.kwargs['pk'])
        if form.instance.business.owner != self.request.user:
            return HttpResponseForbidden()
        return super().form_valid(form)

class ServiceUpdateView(UpdateView):
    model = Service
    template_name = "business/service_update.html"
    form_class = ServiceUpdateForm
    success_url = reverse_lazy('service_detail')

    def get_success_url(self):
        return reverse_lazy('service_detail', kwargs={'pk': self.object.id})

    def get_object(self, queryset=None):
        return Service.objects.get(id=self.kwargs.get('pk'))

class CartListView(ListView):
    model= Cart
    context_object_name= "carts"
    template_name = "business/cart_list.html"

    def get_queryset(self):
     return Cart.objects.filter(user=self.request.user)

def add_to_cart(request, product_id, qty= 1):
    product = get_object_or_404(Product, id=product_id)
    if request.POST['quantity']:
        qty=int(request.POST['quantity'])

    cart, created = Cart.objects.get_or_create(product=product, user=request.user)
    

    if not created:
        cart.quantity += qty

    else:
        cart.quantity=qty
    cart.save()
    messages.success(request, message="succesfull")
    return redirect('product_detail', pk=product_id)

def update_cart(request, product_id):
    item = get_object_or_404(Cart, product__id=product_id)
    item.quantity = request.POST['quantity']
    item.save()
    return redirect('cart')

def remove_from_cart(request, product_id):
    item = get_object_or_404(Cart, product__id=product_id)
    item.delete()
    return redirect('cart')




def checkout(request):
    cart = Cart.objects.all()
    total_cost = 0
    for item in cart:
        total_cost += item.product.price * item.quantity
    context = {
        'cart': cart,
        'total_cost': total_cost,
    }
    return render(request, 'checkout.html', context)

'''def process_payment(request):
    cart = Cart.objects.all()
    # Process payment (omitted for brevity)
    cart.delete()
    return redirect('success')'''



def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    favorites, created = Favorites.objects.get_or_create(product=product, user=request.user)
    if created:
        messages.success(request, "Product added to favorites.")
    return redirect('#')



def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    favorite = get_object_or_404(Favorites, product=product, user=request.user)
    favorite.delete()
    messages.success(request, "Product removed from favorites.")
    return redirect('favorites')


class FavListView(ListView):
    model = Favorites
    context_object_name = "favorites"
    template_name = "business/liked.html"



def rate_product(request, product_id):

    if request.method == 'POST':
        new_rating = request.POST.get('new_rating')
    try:
        # check that the user is authenticated
        if not request.user.is_authenticated:
            return HttpResponseBadRequest("You must be logged in to rate a product")

        # check that the product exists
        product = Product.objects.get(id=product_id)

        # check that the rating value is within the allowed range
        if new_rating < 1 or new_rating > 5:
            return HttpResponseBadRequest("Invalid rating value")

        # check that the user has purchased the product
        # you can add purchase check here
        
        try:
            # check if the user already rated the product
            rating = Rating.objects.get(user=request.user, product=product)
            rating.rating = new_rating
            rating.save()
        except ObjectDoesNotExist:
            # if the rating does not exist, create a new one
            Rating.objects.create(user=request.user, product=product, rating=new_rating)
        
    except Product.DoesNotExist:
        return HttpResponseBadRequest("Invalid product id")
    except IntegrityError:
        return HttpResponseBadRequest("You have already rate this product")
    return HttpResponse("Product rated successfully")



def rate_service(request, pk):

    if request.method == 'POST':
        new_rating = int(request.POST.get('new_rating'))
    try:
        # check that the user is authenticated
        if not request.user.is_authenticated:
            return HttpResponseBadRequest("You must be logged in to rate a product")

        # check that the product exists
        service = Service.objects.get(id=pk)

        # check that the rating value is within the allowed range
        if new_rating < 1 or new_rating > 5:
            return HttpResponseBadRequest("Invalid rating value")

        # check that the user has purchased the product
        # you can add purchase check here
        
        try:
            # check if the user already rated the product
            rating = Rating.objects.get(user=request.user, service=service)
            rating.rating = new_rating
            rating.save()
        except ObjectDoesNotExist:
            # if the rating does not exist, create a new one
            Rating.objects.create(user=request.user, service=service, rating=new_rating)
        
    except Product.DoesNotExist:
        return HttpResponseBadRequest("Invalid product id")
    except IntegrityError:
        return HttpResponseBadRequest("You have already rate this product")
    return HttpResponse("Product rated successfully")

# search
def SearchResultsListView(request):
    query = request.GET.get("q")


    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )

    services = Service.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )

    business = Business.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )

    service_business = ServiceBusiness.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )

    context = {
        'products': products,
        'business': business,
        'services': services,
        'service_business': service_business,
    }
    return render(request, 'search_results.html', context)

def category_search(request, category):
    products = Product.objects.filter(
        Q(category__icontains=category)
    )

    #services = Services.objects.filter(
    #    Q(category__icontains=category)
    #)

    business = Business.objects.filter(
        Q(category__icontains=category)
    )

    context = {
        'products': products,
        'businesses': business,
    }
    return render(request, 'business/category_search.html', context)

def service_category_search(request, category):
    pass
