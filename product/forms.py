from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(label='Граммы продукта')
    product_id = forms.IntegerField()
