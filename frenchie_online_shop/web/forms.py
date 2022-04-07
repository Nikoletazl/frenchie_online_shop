from django import forms

from frenchie_online_shop.web.models import Category, Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        max_length=Product.TITLE_MAX_LENGTH,
    )

    description = forms.Textarea(
    )

    image = forms.ImageField()

