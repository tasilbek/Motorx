from django.urls import path
from .views import *

urlpatterns = [
    path('404', Page404View.as_view(), name='404'),
    path('addcart', AddcartPageView.as_view(), name='addcart'),
    path('blog-single', BlogSinglePageView.as_view(), name='blog-single'),
    path('blog', BlogPageView.as_view(), name='blog'),
    path('car-list', CarListPageView.as_view(), name='car-list'),
    path('contact-us', ContactUsPageView.as_view(), name='contact-us'),
    path('dashboard', DashboardPageView.as_view(), name='dashboard'),
    path('dealer-details', DealerDetailsPageView.as_view(), name='dealer-details'),
    path('home02', Home2PageView.as_view(), name='home02'),
    path('home03', Home3PageView.as_view(), name='home03'),
    path('home04', Home4PageView.as_view(), name='home04'),
    path('home05', Home5PageView.as_view(), name='home05'),
    path('home06', Home6PageView.as_view(), name='home06'),
    path('', HomePageView.as_view(), name='home'),
    path('listing-details', ListingDetailsPageView.as_view(), name='listing-details'),
    path('my-inventory', MyInventoryPageView.as_view(), name='my-inventory'),
    path('seller-profile', SellerProfilePageView.as_view(), name='seller-profile')
]
