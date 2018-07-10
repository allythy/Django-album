from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.generic import TemplateView, ListView

from album.models import Foto


class IndexView(ListView):
    template_name = 'album/index.html'
    queryset = Foto.objects.filter(aprovado=True).all()


class AvaliacaoFotosView(ListView):
    template_name = 'album/avaliacao.html'
    queryset = Foto.objects.filter(aprovado=None).all()


class AprovarFotosView(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class AprovarFotosView(LoginRequiredMixin, TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
