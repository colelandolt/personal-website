from django.urls import path

from . import views as page_views

urlpatterns = [
    path('', page_views.home_page),
    path('about/', page_views.about_page),
]
