from django.shortcuts import render
from django.views.generic import TemplateView
from business.models import Product,Service

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newest_products'] = Product.objects.all().order_by('-date_created')[:10]
        context['popular_products'] = Product.objects.all().order_by('-views')[:10]
        context['highest_rated_products'] = Product.objects.all().order_by('-average_rating')[:10]
        context['newest_services'] = Service.objects.all().order_by('-date_created')[:10]
        context['popular_services'] = Service.objects.all().order_by('-views')[:10]
        context['highest_rated_services'] = Service.objects.all().order_by('-average_rating')[:10]
        return context


class SortPageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,request, **kwargs):
        context = super().get_context_data(**kwargs)
        order_by = request.GET.get('order_by')

        if order_by=='most_popular':
            context['popular_products'] = Product.objects.all().order_by('-views')
            context['popular_services'] = Service.objects.all().order_by('-views')

        elif order_by=='newest':
            context['newest_products'] = Product.objects.all().order_by('-date_created')
            context['newest_services'] = Service.objects.all().order_by('-date_created')

        elif order_by=='most_rated':
            context['highest_rated_products'] = Product.objects.all().order_by('-average_rating')
            context['highest_rated_services'] = Service.objects.all().order_by('-average_rating')

        return context






