from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request)
    print(request.user)
    print(args)
    print(kwargs)
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "this is about us",
        "my_number": 41,
        "my_list": [123, 456, 789, 0],
        "this_is_true": True,
        "html_text": "<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)
