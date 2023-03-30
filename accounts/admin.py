from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserProfile


class ProfileInline(admin.TabularInline):
    model= UserProfile

CustomUser=get_user_model()
class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=["email","username","residential_address","is_superuser",]

    fieldsets= UserAdmin.fieldsets + ((None, {"fields":("residential_address",)}),)
    add_fieldsets= UserAdmin.add_fieldsets + ((None, {"fields":("email","residential_address",)}),)

    inlines= [
        ProfileInline
    ]




class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
