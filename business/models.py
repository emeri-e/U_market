from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid

# Create your models here.

class Business(models.Model):
    id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False)
    name = models.CharField(max_length=200)
    ProfilePix = models.ImageField(upload_to="BuzProfile/", blank=True)
    description = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    

    owner = models.OneToOneField( get_user_model(), on_delete=models.CASCADE, related_name= "business" )

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("Buz_detail", kwargs={'pk':self.id})


class ServiceBusiness(models.Model):
    id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False)
    name = models.CharField(max_length=200)
    ProfilePix = models.ImageField(upload_to="ServiceBuzProfile/", blank=True)
    description = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    

    owner = models.OneToOneField( get_user_model(), on_delete=models.CASCADE, related_name= "service_business" )

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("service_detail", kwargs={'pk':self.id})


class Product(models.Model):
    id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="ProductPix/", blank=True)
    description = models.TextField(max_length=1000)
    category = models.CharField(choices=(("1","Mens Body wears"), ("2","Women Body wears"),("3","Unisex Body wears"),("4","Educational"),("5","Sports"),("6","Food"),("7","Others")), max_length=20, default="Others")
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    views = models.IntegerField(default=0)
    product_count = models.IntegerField()
    average_rating = models.FloatField(default=0.0)
    

    business = models.ForeignKey( Business, on_delete=models.CASCADE, related_name= "products" , editable=False)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'pk':self.id})

    def update_count(self,new_count):
        self.count= new_count

class Service(models.Model):
    id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="ServicePix/", blank=True)
    description = models.TextField(max_length=1000)
    category = models.CharField(choices=(("1","Educational"),("2","Sports"),("3","Food"),("4","Cleaning"),("5","Others")), max_length=20, default="Others")
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    views = models.IntegerField(default=0)
    business = models.ForeignKey( ServiceBusiness, on_delete=models.CASCADE, related_name= "services" , editable=False)
    average_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("service_detail", kwargs={'pk':self.id})

class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    
class Favorites(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,related_name='reviews', null=True, blank=True)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

class ServiceReview(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL,related_name='reviews', null=True, blank=True)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

class Rating(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='ratings')
    service = models.OneToOneField(Service, on_delete=models.CASCADE, null=True, blank=True, related_name='ratings')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'product',)
        unique_together = ('user', 'service',)
    
