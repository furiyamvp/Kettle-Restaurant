from django.urls import path
from pages.views import *

app_name = "products"

urlpatterns = [
    path("", home_page_view, name="home"),
    path("about/", about_page_view, name="about"),
    path("blog/", blog_page_view, name="blog"),
]
