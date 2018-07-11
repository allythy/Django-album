from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, View, CreateView

from album.models import Foto


class IndexView(SuccessMessageMixin, CreateView, ListView):
    success_message = 'Sua foto foi enviada com sucesso!'
    template_name = 'album/index.html'
    queryset = Foto.objects.filter(aprovado=True).all()
    model = Foto
    success_url = reverse_lazy('index')
    fields = ['imagem']


class AvaliacaoFotosView(LoginRequiredMixin, TemplateView):
    template_name = 'album/avaliacao.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['aprovadas'] = Foto.objects.filter(aprovado=True).all()
        context['pendentes'] = Foto.objects.filter(aprovado=None).all()
        context['rejeitadas'] = Foto.objects.filter(aprovado=False).all()
        return context


class AprovarFotoView(LoginRequiredMixin, View):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        foto = get_object_or_404(Foto, id=kwargs['foto_id'])
        foto.aprovado = kwargs['aprovacao']
        foto.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

