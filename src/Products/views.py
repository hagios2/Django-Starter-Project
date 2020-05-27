from django.shortcuts import render

from Products.models import Product

# Create your views here.
def view_product_detail(request):

    obj = Product.objects.get(id=1)

    context = {

        'title': obj.title,
        'description': obj.description,
        'summary': obj.summary
    }

    return render(request, 'products/details.html', context)