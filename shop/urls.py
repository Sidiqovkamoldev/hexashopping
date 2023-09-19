from django.urls import path
from .views import HomePageView, product_detail, ContactPageView, CategoryPageView, categoryview



urlpatterns = [
        path("home/", HomePageView.as_view(), name='home_page_view'),
        path('products/create/', ContactPageView.as_view(), name='create_client_view'),
        path('product/<slug:product>/', product_detail, name='product_detail_view'),
        path('category/', CategoryPageView.as_view(), name='categories_detail_view'),
        path('category/<slug:product_id>/', categoryview, name='category_detail_view')

]