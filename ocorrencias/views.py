from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ocorrencia, Bairro
from .forms import BairroForm, OcorrenciaForm




# View do dashboard, que exibe as ocorrências e os totalizadores
@login_required
def dashboard(request):
    # Captura os parâmetros de busca
    bairro_id = request.GET.get('bairro')
    status_filtro = request.GET.get('status')

    # Totalizadores para os Cards
    total_ocorrencias = Ocorrencia.objects.count()
    em_andamento = Ocorrencia.objects.filter(status='EM_ANDAMENTO').count()
    resolvidas = Ocorrencia.objects.filter(status='RESOLVIDO').count()

    # Consulta para a listagem
    ocorrencias = Ocorrencia.objects.select_related('bairro', 'responsavel').all()

    # Lista ocorrências em andamento para o mapa
    ocorrencias_mapa = Ocorrencia.objects.filter(status='EM_ANDAMENTO').select_related('bairro')

    # Aplica os filtros se houverem
    if bairro_id:
        ocorrencias = ocorrencias.filter(bairro_id=bairro_id)
    if status_filtro:
        ocorrencias = ocorrencias.filter(status=status_filtro)

    bairros = Bairro.objects.all()

    dados_mapa = [
        {
            'bairro': item.bairro.nome,
            'lat': item.bairro.latitude,
            'lng': item.bairro.longitude,
            'data_hora': item.data_hora.strftime('%d/%m/%Y %H:%M'),
            'descricao': item.descricao
        }
        for item in ocorrencias_mapa if item.bairro.latitude and item.bairro.longitude
    ]

    context = {
        'total_ocorrencias': total_ocorrencias,
        'em_andamento': em_andamento,
        'resolvidas': resolvidas,
        'ocorrencias': ocorrencias,
        'ocorrencias_mapa': ocorrencias_mapa,
        'bairros': bairros,
        'bairro_selecionado': bairro_id,
        'status_selecionado': status_filtro,
        'dados_mapa_json': dados_mapa,
    }

    return render(request, 'ocorrencias/dashboard.html', context)

# CRUD de bairros
@login_required
def criar_bairro(request):
    if request.method == 'POST':
        form = BairroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BairroForm()

    return render(request, 'ocorrencias/bairro_form.html', {'form': form})

@login_required
def listar_bairros(request):
    bairros = Bairro.objects.all()
    return render(request, 'ocorrencias/bairros_list.html', {'bairros': bairros})

# Editar bairro
@login_required
def editar_bairro(request, pk):
    bairro = Bairro.objects.get(pk=pk)
    if request.method == 'POST':
        form = BairroForm(request.POST, instance=bairro)
        if form.is_valid():
            form.save()
            return redirect('listar_bairros')
    else:
        form = BairroForm(instance=bairro)

    return render(request, 'ocorrencias/bairro_form.html', {'form': form})

# Exluir bairro
@login_required
def excluir_bairro(request, pk):
    bairro = Bairro.objects.get(pk=pk)
    if request.method == 'POST':
        bairro.delete()
        return redirect('listar_bairros')
    return render(request, 'ocorrencias/bairro_confirm_delete.html', {'bairro': bairro})

# Criar ocorrência
@login_required
def criar_ocorrencia(request):
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = OcorrenciaForm(initial={'responsavel': request.user})

    return render(request, 'ocorrencias/ocorrencia_form.html', {'form': form})

# Editar ocorrência
@login_required
def editar_ocorrencia(request, pk):
    ocorrencia = Ocorrencia.objects.get(pk=pk)
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, instance=ocorrencia)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = OcorrenciaForm(instance=ocorrencia)

    return render(request, 'ocorrencias/ocorrencia_form.html', {'form': form})

# Excluir ocorrência
@login_required
def excluir_ocorrencia(request, pk):
    ocorrencia = Ocorrencia.objects.get(pk=pk)
    if request.method == 'POST':
        ocorrencia.delete()
        return redirect('dashboard')
    return render(request, 'ocorrencias/ocorrencia_confirm_delete.html', {'ocorrencia': ocorrencia})

