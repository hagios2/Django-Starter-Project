from django.shortcuts import render

from Products.models import Product

from Products.forms import ProductForm, RawProductForm

# Create your views here.
def view_product_detail(request):

    obj = Product.objects.get(id=1)

    context = {'object' : obj}

    return render(request, 'products/details.html', context)


def view_product_form(request):
 
    form = ProductForm(request.POST or None)

    if form.is_valid():


        # Product.objects.create(**form.cleaned_data)

        form.save()

        form = ProductForm()

    context = {'form' : form}

    return render(request, 'products/product_form.html', context)


# def view_product_form(request):

     
#     form = RawProductForm()

#     if request.method == 'POST':

#         form = RawProductForm(request.POST)

#         if form.is_valid():

#             print(form.cleaned_data)

#             Product.objects.create(**form.cleaned_data)
        
#         else:

#             print(form.errors)


    # context = {'form' : form}

    # return render(request, 'products/product_form.html', context)

    