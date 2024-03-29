from django.shortcuts import render, redirect, get_object_or_404
from .models import Ativo, Passivo
from .forms import AtivoForm, PassivoForm

def adicionar_ativo(request):
    if request.method == 'POST':
        ativo_form = AtivoForm(request.POST)
        if ativo_form.is_valid():
            ativo_form.save()
            return redirect('ativos_listagem')
    else:
        ativo_form = AtivoForm()
    
    return render(request, 'balanco/adicionar_ativo.html', {'ativo_form': ativo_form})

def editar_ativo(request, ativo_id):
    ativo = get_object_or_404(Ativo, pk=ativo_id)

    if request.method == 'POST':
        ativo_form = AtivoForm(request.POST, instance=ativo)
        if ativo_form.is_valid():
            ativo_form.save()
            return redirect('ativos_listagem')
    else:
        ativo_form = AtivoForm(instance=ativo)
    
    return render(request, 'balanco/editar_ativo.html', {'ativo_form': ativo_form})

def apagar_ativo(request, ativo_id):
    ativo = get_object_or_404(Ativo, pk=ativo_id)
    if request.method == 'POST':
        ativo.delete()
        return redirect('ativos_listagem')
    return render(request, 'balanco/apagar_ativo.html', {'ativo': ativo})

def ativos_listagem(request):
    ativos = Ativo.objects.all()
    return render(request, 'balanco/ativos_listagem.html', {'ativos': ativos})

def adicionar_passivo(request):
    if request.method == 'POST':
        passivo_form = PassivoForm(request.POST)
        if passivo_form.is_valid():
            passivo_form.save()
            return redirect('passivos_listagem')
    else:
        passivo_form = PassivoForm()
    
    return render(request, 'balanco/adicionar_passivo.html', {'passivo_form': passivo_form})

def editar_passivo(request, passivo_id):
    passivo = get_object_or_404(Passivo, pk=passivo_id)

    if request.method == 'POST':
        passivo_form = PassivoForm(request.POST, instance=passivo)
        if passivo_form.is_valid():
            passivo_form.save()
            return redirect('passivos_listagem')
    else:
        passivo_form = PassivoForm(instance=passivo)
    
    return render(request, 'balanco/editar_passivo.html', {'passivo_form': passivo_form})

def apagar_passivo(request, passivo_id):
    passivo = get_object_or_404(Passivo, pk=passivo_id)
    if request.method == 'POST':
        passivo.delete()
        return redirect('passivos_listagem')
    return render(request, 'balanco/apagar_passivo.html', {'passivo': passivo})

def passivos_listagem(request):
    passivos = Passivo.objects.all()
    return render(request, 'balanco/passivos_listagem.html', {'passivos': passivos})

def balanco_patrimonial(request):
    ativos = Ativo.objects.all()
    passivos = Passivo.objects.all()

    total_ativos = sum(ativo.valor for ativo in ativos)
    total_passivos = sum(passivo.valor for passivo in passivos)

    patrimonio_liquido = total_ativos - total_passivos

    context = {
        'ativos': ativos,
        'passivos': passivos,
        'total_ativos': total_ativos,
        'total_passivos': total_passivos,
        'patrimonio_liquido': patrimonio_liquido
    }

    return render(request, 'balanco/balanco_patrimonial.html', context)

