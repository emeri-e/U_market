from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import UserProfile
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields = (
            'username',
            'email',
            'residential_address'
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=get_user_model()
        fields = (
            'username',
            'email',
            'residential_address'
        )

class ProfileUpdateForm(ModelForm):
    class Meta:
        model=UserProfile
        fields = ['firstname','lastname','username','date_of_birth', 'photo', 'phone']

