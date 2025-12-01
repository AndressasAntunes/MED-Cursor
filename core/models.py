from django.db import models
from django.utils import timezone


class Transacao(models.Model):
    TIPO_CHOICES = [
        ('RECEITA', 'Receita'),
        ('DESPESA', 'Despesa'),
    ]
    
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(default=timezone.now)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    
    class Meta:
        ordering = ['-data']
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
    
    def __str__(self):
        return self.descricao

