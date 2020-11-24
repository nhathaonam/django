from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


#def homePageView(request):
 #   return HttpResponse('Hello, This is page test')

class HomeBase(TemplateView):
    template_name = 'base.html'

class HomePageView(TemplateView):
    template_name = 'home.html'
    

class AboutView(TemplateView):
    template_name = 'about.html'

    