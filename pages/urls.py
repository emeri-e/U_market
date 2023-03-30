from django.urls import path
from .views import HomePageView, SortPageView


urlpatterns = [
path("", HomePageView.as_view(), name="home"),
path("sort/<order_by>", SortPageView.as_view(), name="sort"),


]
