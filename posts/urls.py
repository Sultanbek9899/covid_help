from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('helpform', views.help_form, name='help_form'),
    path('requests/', views.requests_list, name='requests_list'),
    path('offers/', views.offers_list, name='offers_list')
]