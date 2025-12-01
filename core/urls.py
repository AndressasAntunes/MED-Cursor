from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.adicionar_transacao, name='adicionar_transacao'),
    path('excluir/<int:pk>/', views.excluir_transacao, name='excluir_transacao'),
]

