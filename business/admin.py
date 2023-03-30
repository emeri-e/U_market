from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Business, Product, Cart, Favorites, Review,ServiceReview, Service,ServiceBusiness

class PrductInline(admin.TabularInline):
    model= Product

class ServiceInline(admin.TabularInline):
    model= Service

class ReviewInline(admin.TabularInline):
    model= Review

class ServiceReviewInline(admin.TabularInline):
    model= ServiceReview


class BuzAdmin(admin.ModelAdmin):
    list_display = ("name", "owner",)
    inlines= [
        PrductInline
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "business",)
    inlines= [
        ReviewInline
    ]
    
class ServiceBuzAdmin(admin.ModelAdmin):
    list_display = ("name", "owner",)
    inlines= [
        ServiceInline
    ]

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "business",)
    inlines= [
        ServiceReviewInline
    ]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "product","created")
    
class ServiceReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "service","created")
    

class CartAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity",)
    
class FavAdmin(admin.ModelAdmin):
    list_display = ("product", "user",)
    




admin.site.register(Business, BuzAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Favorites, FavAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ServiceReview, ServiceReviewAdmin)
admin.site.register(ServiceBusiness, ServiceBuzAdmin)
admin.site.register(Service, ServiceAdmin)


