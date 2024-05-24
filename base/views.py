from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Page404View(TemplateView):
    template_name = 'pages/404.html'
class AddcartPageView(TemplateView):
    template_name = 'pages/addcart.html'
class BlogSinglePageView(TemplateView):
    template_name = 'pages/blog-single.html'
class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'
class CarListPageView(TemplateView):
    template_name = 'pages/car-list.html'
class ContactUsPageView(TemplateView):
    template_name = 'pages/contact-us.html'
class DashboardPageView(TemplateView):
    template_name = 'pages/dashboard.html'
class DealerDetailsPageView(TemplateView):
    template_name = 'pages/dealer-details.html'
class Home2PageView(TemplateView):
    template_name = 'pages/home02.html'
class Home3PageView(TemplateView):
    template_name = 'pages/home03.html'
class Home4PageView(TemplateView):
    template_name = 'pages/home04.html'
class Home5PageView(TemplateView):
    template_name = 'pages/home05.html'
class Home6PageView(TemplateView):
    template_name = 'pages/home06.html'
class HomePageView(TemplateView):
    template_name = 'pages/index.html'
class ListingDetailsPageView(TemplateView):
    template_name = 'pages/listing-details.html'
class MyInventoryPageView(TemplateView):
    template_name = 'pages/my-inventory.html'
class SellerProfilePageView(TemplateView):
    template_name = 'pages/seller-profile.html'
