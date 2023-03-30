from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from .models import Rating

@receiver(post_save, sender=Rating)
def update_average_rating(sender, instance, **kwargs):
    product = instance.product
    service = instance.service
    if product:
        ratings = Rating.objects.filter(product=product)
        if ratings.exists():
            product.average_rating = ratings.aggregate(Avg('rating'))['rating__avg']
            product.save()
    if service:
        ratings = Rating.objects.filter(service=service)
        if ratings.exists():
            service.average_rating = ratings.aggregate(Avg('rating'))['rating__avg']
            service.save()

