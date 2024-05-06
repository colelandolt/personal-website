from django.shortcuts import render

from .models import Subscriber
from .forms import SubscriberModelForm

def home_page(request, *args, **kwargs):
    title = "Home"
    form = SubscriberModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save()

    context = {
        "title": title,
        "form": form
    }
    return render(request, "pages/home.html", context)

def about_page(request, *args, **kwargs):
    title = "About"
    context = {
        "title": title
    }
    return render(request, "about.html", context)