from django.shortcuts import render


def home_page(request, *args, **kwargs):
    context = {
        "title": "Home"
    }
    return render(request, "home.html", context)

def about_page(request, *args, **kwargs):
    context = {
        "title": "About"
    }
    return render(request, "about.html", context)