from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Q
from .models import Transacao
from .forms import TransacaoForm


def home(request):
    transacoes = Transacao.objects.all().order_by('-data')
    
    # Calcular saldo total (Receitas - Despesas)
    receitas = Transacao.objects.filter(tipo='RECEITA').aggregate(
        total=Sum('valor')
    )['total'] or 0
    
    despesas = Transacao.objects.filter(tipo='DESPESA').aggregate(
        total=Sum('valor')
    )['total'] or 0
    
    saldo_total = receitas - despesas
    
    context = {
        'transacoes': transacoes,
        'saldo_total': saldo_total,
        'receitas_total': receitas,
        'despesas_total': despesas,
    }
    
    return render(request, 'core/index.html', context)


def adicionar_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransacaoForm()
    
    return render(request, 'core/adicionar.html', {'form': form})


def excluir_transacao(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk)
    if request.method == 'POST':
        transacao.delete()
        return redirect('home')
    
    # GET request - mostrar página de confirmação
    return render(request, 'core/excluir.html', {'transacao': transacao})

