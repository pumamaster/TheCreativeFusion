from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Photo

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.all().order_by('-id')
        return context


