from django import forms

class SearchForm(forms.Form):
    product_name = forms.CharField(max_length=100, label="Nom du produit")
class ProductSearchForm(forms.Form):
    product_name = forms.CharField(
        label='Nom du produit',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Recherchez un produit...',
            'class': 'form-control',
        })
    )
