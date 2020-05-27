from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'home.html')


def contact_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'contact.html')

def about_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello World</h1>')

    my_context = {

        "info": "this is about our company ....",
        "Num_workers": 2000,
        "mylist" : ['Joshua', 'Prince', 'Claudy', 'Gidi'],
        "numbs": [100, 125, 300, 2000, 500, 5000, 6000]
    }

    return render(request, 'about.html', my_context)