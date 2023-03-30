from django.urls import path
from .views import BUzListView,ServiceBUzDetailView,ServiceBuzUpdateView,ServiceBuzCreateView,ServiceCreateView,ServiceDetailView,ServiceUpdateView, FavListView, ProductCreateView, ProductListView, BuzCreateView,BuzUpdateView, BUzDetailView, ProductDetailView, ProductUpdateView, ServiceListView, ServiceDetailView, SearchResultsListView, add_to_cart, rate_product, rate_service,update_cart,remove_from_cart, CartListView, add_to_favorites, category_search, service_category_search #MyBuzListView

urlpatterns = [
    path("", BUzListView.as_view(), name="Buz_list"),
    path("<uuid:pk>/", BUzDetailView.as_view(), name="Buz_detail"),
    path("create/", BuzCreateView.as_view(), name="Buz_create"),
    path("update/<uuid:pk>/", BuzUpdateView.as_view(), name="Buz_update"),

    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/detail/<uuid:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/create/<uuid:pk>/", ProductCreateView.as_view(), name="product_create"),
    path("products/update/<uuid:pk>/", ProductUpdateView.as_view(), name="product_update"),

    path("servicebuz/<uuid:pk>/", ServiceBUzDetailView.as_view(), name="ServiceBuz_detail"),
    path("servicebuz/create/", ServiceBuzCreateView.as_view(), name="ServiceBuz_create"),
    path("servicebuz/update/<uuid:pk>/", ServiceBuzUpdateView.as_view(), name="ServiceBuz_update"),

    path("services/", ServiceListView.as_view(), name="service_list"),
    path("services/detail/<uuid:pk>/", ServiceDetailView.as_view(), name="service_detail"),
    path("services/create/<uuid:pk>/", ServiceCreateView.as_view(), name="service_create"),
    path("services/update/<uuid:pk>/", ServiceUpdateView.as_view(), name="service_update"),

    path("add_to_cart/<uuid:product_id>", add_to_cart, name="add_to_cart"),
    path("cart", CartListView.as_view(), name="cart"),
    path('update/<uuid:product_id>/', update_cart, name='update_cart'),
    path('remove/<uuid:product_id>/', remove_from_cart, name='remove_from_cart'),


    path("add_to_favorites/<uuid:pk>", add_to_favorites, name="add_to_favorites"),
    path("favorites", FavListView.as_view(), name="liked"),
   # path("my_Buz", MyBuzListView.as_view(), name="my_Buz_list"),
   
    path("service/rate/<uuid:pk>", rate_service, name="rate_service"),
    path("product/rate/<uuid:pk>", rate_product, name="rate_product"),

    path("search/", SearchResultsListView, name="search_results"),
    path("categories/<category>", category_search, name="category_search"),
    path("categories/services/<category>", service_category_search, name="service_category_search"),

]
