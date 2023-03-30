

from django.forms import ModelForm
from .models import Business, Product, ServiceBusiness, Service


class BuzUpdateForm(ModelForm):
    class Meta:
        model=Business
        fields=["name",'description', 'location','ProfilePix']

class ProductUpdateForm(ModelForm):
    class Meta:
        model=Product
        fields=["name",'description', 'category', 'price','photo', 'product_count']


class ServiceBuzUpdateForm(ModelForm):
    class Meta:
        model=ServiceBusiness
        fields=["name",'description', 'location','ProfilePix']

class ServiceUpdateForm(ModelForm):
    class Meta:
        model=Service
        fields=["name",'description', 'category', 'price','photo']
        
