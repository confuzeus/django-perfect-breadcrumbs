from django.shortcuts import render
from django.urls import reverse_lazy


def home(request):
    return render(request, "testapp/index.html")


def about(request):
    request.breadcrumb_builder.add("Home", reverse_lazy("home"))
    request.breadcrumb_builder.add("About", active=True)
    return render(request, "testapp/about.html")


def about_josh(request):
    breadcrumbs = [
        {"name": "Home", "url": reverse_lazy("home")},
        {"name": "about", "url": reverse_lazy("about")},
        {"name": "About Josh", "active": True},
    ]
    request.breadcrumb_builder.add_bulk(breadcrumbs)
    return render(request, "testapp/josh.html")
