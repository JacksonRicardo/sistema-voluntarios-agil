from django.urls import path
from .views import VoluntarioCreateView, cadastro_sucesso

urlpatterns = [
    path('', VoluntarioCreateView.as_view(), name='cadastro_voluntario'),
    path('sucesso/', cadastro_sucesso, name='cadastro_sucesso'),
]
