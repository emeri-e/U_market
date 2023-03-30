#import sqlite3
import uuid
from django.shortcuts import get_object_or_404, render , redirect
import threading , time

from django.urls import reverse_lazy
from .models import UserProfile
from django.views.generic import UpdateView, DetailView
from .forms import ProfileUpdateForm
# Create your views here.


def real_profile_update(request):
    try:
        profile, created = UserProfile.objects.get_or_create(user=request.user, email=request.user.email)
        if not created:
            profile.email = request.user.email
            
        profile.save()

    except:
        profile=UserProfile.objects.get(user=request.user)
        profile.email = request.user.email
        profile.save()
    

def update_profile(request):
    threadObj = threading.Thread(target=real_profile_update, args=[request,])
    threadObj.start()
    
    

    return redirect('home')

class ProfileEditView(UpdateView):
    model = UserProfile
    template_name = "profile_edit.html"
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('profile_detail')

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'Puuid': self.object.Puuid})

    def get_object(self, queryset=None):
        return UserProfile.objects.get(Puuid=self.kwargs.get('Puuid'))



class ProfileDetailView(DetailView):
    model = UserProfile
    template_name = "profile_detail.html"


    def get(self, request, *args, **kwargs):
        product_uuid = self.kwargs.get('Puuid')
        profile = get_object_or_404(UserProfile, Puuid=product_uuid)
        context = {'profile':profile}
        return render(request, self.template_name, context)

    

    


    






