from django.shortcuts import render
from djongo import models
from .forms import ProductSearchForm
from .models import Product


# Importer les modèles des collections TunisiaNet et MyTek
def home(request):
    return render(request, 'comparateur/home.html')

class TunisiaNetProduct(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255)

    class Meta:
        db_table = "tunisia_net"


class MyTekProduct(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255)

    class Meta:
        db_table = "MyTek"


# Vue pour le comparateur
def compare_prices(request):
    form = ProductSearchForm(request.GET or None)
    results = []
    cheapest_site = None
    cheapest_price = None

    if request.GET.get('product_name'):
        product_name = request.GET['product_name']

        # Recherche dans TunisiaNet
        tunisianet_results = TunisiaNetProduct.objects.filter(title__icontains=product_name)

        # Recherche dans MyTek
        mytek_results = MyTekProduct.objects.filter(title__icontains=product_name)

        # Comparer les prix si les résultats existent
        for product in tunisianet_results:
            results.append({
                'title': product.title,
                'price': product.price,
                'site': 'TunisiaNet'
            })

        for product in mytek_results:
            results.append({
                'title': product.title,
                'price': product.price,
                'site': 'MyTek'
            })

        # Trouver le prix le moins cher
        if results:
            cheapest_product = min(results, key=lambda x: x['price'])
            cheapest_price = cheapest_product['price']
            cheapest_site = cheapest_product['site']

    return render(request, 'comparateur/compare_prices.html', {
        'form': form,
        'results': results,
        'cheapest_site': cheapest_site,
        'cheapest_price': cheapest_price
    }
                  )
