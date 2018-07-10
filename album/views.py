from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'album/index.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class EditarAlbumView(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        kwargs['algumacoisa'] = 'ASDALdASDLasdlasDAsdASLd Teste'
        return super().get_context_data(**kwargs)
