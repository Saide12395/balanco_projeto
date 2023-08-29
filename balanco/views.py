from django.shortcuts import render, redirect
from .models import Ativo, Passivo
from .forms import AtivoForm, PassivoForm

def balanco_patrimonial(request):
    ativos = Ativo.objects.all()
    passivos = Passivo.objects.all()
    
    total_ativos = sum(ativo.valor for ativo in ativos)
    total_passivos = sum(passivo.valor for passivo in passivos)
    patrimonio_liquido = total_ativos - total_passivos
    
    if request.method == 'POST':
        ativo_form = AtivoForm(request.POST)
        passivo_form = PassivoForm(request.POST)
        
        if ativo_form.is_valid():
            ativo_form.save()
            return redirect('balanco_patrimonial')
        
        if passivo_form.is_valid():
            passivo_form.save()
            return redirect('balanco_patrimonial')
    else:
        ativo_form = AtivoForm()
        passivo_form = PassivoForm()
    
    return render(request, 'balanco/balanco.html', {
        'ativos': ativos,
        'passivos': passivos,
        'total_ativos': total_ativos,
        'total_passivos': total_passivos,
        'patrimonio_liquido': patrimonio_liquido,
        'ativo_form': ativo_form,
        'passivo_form': passivo_form,
    })
