from django.shortcuts import render

from .forms import LandingPageForm

def home_page(request, *args, **kwargs):
    title = "Home"
    form = LandingPageForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data.get("email"))
        form = LandingPageForm()

    context = {
        "title": title,
        "form": form
    }
    return render(request, "home.html", context)

def about_page(request, *args, **kwargs):
    title = "About"
    context = {
        "title": title
    }
    return render(request, "about.html", context)