from django.urls import path
from . import views

urlpatterns = [
    path('' , views.inicio , name='inicio'),
    path('about' , views.about , name='about'),
    path('pacientes' , views.pacientes , name='pacientes'),
    path('pacientes/crear' , views.crear , name="crear"),
    path('pacientes/editar/<int:id>' , views.editar , name="editar"),
    path('borrar/<int:id>' , views.borrar , name="borrar")
]