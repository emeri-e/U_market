from django.urls import path
from .views import ProfileEditView,ProfileDetailView, update_profile


urlpatterns = [
    path('update_profile/', update_profile, name='update_profile'),

    path('profile_detail/<uuid:Puuid>/',ProfileDetailView.as_view() , name='profile_detail'),
    path('profile_edit/<uuid:Puuid>/',ProfileEditView.as_view() , name='profile_edit'),


]