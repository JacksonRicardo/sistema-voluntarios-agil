from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from .models import Voluntario
from .forms import VoluntarioForm

class VoluntarioCreateView(CreateView):
    model = Voluntario
    form_class = VoluntarioForm
    template_name = 'voluntarios/cadastro.html'
    success_url = reverse_lazy('cadastro_sucesso')

def cadastro_sucesso(request):
    return render(request, 'voluntarios/sucesso.html')
