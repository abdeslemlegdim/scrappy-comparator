from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('compare/', views.compare_prices, name='compare_prices'),  # Page de recherche
]
