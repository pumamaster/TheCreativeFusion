from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Photo, Fondo

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(vertical=True).order_by('-id')
        context['fondo'] = Fondo.objects.first()
        return context
    
class Index2(TemplateView):
    template_name = "index2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(vertical=False).order_by('-id')
        context['fondo'] = Fondo.objects.first()
        return context


