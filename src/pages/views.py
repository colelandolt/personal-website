from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Subscriber
from .forms import SubscriberModelForm

def home_page(request, *args, **kwargs):

    title = "Home"
    form = SubscriberModelForm(request.POST or None)
    request.session['subscribed'] = False
    if form.is_valid():
        obj = form.save()
        messages.success(request, "Thanks for joining!", extra_tags="alert-success")
        request.session['subscribed'] = True
        return HttpResponseRedirect("/")

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
    return render(request, "pages/about.html", context)