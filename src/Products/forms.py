from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    #customizing form fields and front end validation

    #recommended practice use same names as field name in db

    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "custom placeholder"}))
    description = forms.CharField(

        required = False,
        widget =forms.Textarea(attrs={
            "placeholder":"Your description",
            "class": "form-control",
            "id":"desc",
            "rows":10,
            "cols": 25

        })
    )

    price = forms.DecimalField()

    # class Meta:
    #     model = Product
    #     fields = ['title', 'description', 'price']
    
    def clean_title(self, *args, **kwargs):

        title = self.cleaned_data.get('title')

        if len(title) < 8:
            raise forms.ValidationError("This has shorter chars")
        else:
            return title
         

class RawProductForm(forms.Form):

    pass

#     title       = forms.CharField()
#     description = forms.CharField();
#     price       = forms.DecimalField()