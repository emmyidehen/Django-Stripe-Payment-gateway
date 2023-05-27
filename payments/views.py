from django.shortcuts import render


# Create your views here.
#In payment/urls.py

from django.views.generic.base import TemplateView



class HomeView(TemplateView):    
     template_name = 'home.html'

     

     