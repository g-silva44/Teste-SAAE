from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Bairro, Ocorrencia
from django.utils import timezone

class BairroModelTest(TestCase):
    def setUp(self):
        # Cria um bairro de teste
        self.bairro = Bairro.objects.create(
            nome="Centro",
            latitude=-9.4137,
            longitude=-40.5036
        )

    def test_bairro_str(self):
    # Testa a representação em texto do modelo Bairro
        self.assertEqual(str(self.bairro), "Centro")

    def test_bairro_coordenadas(self):
    # Garante que as coordenadas são salvas como números com ponto decimal
        self.assertEqual(self.bairro.latitude, -9.4137)
        self.assertEqual(self.bairro.longitude, -40.5036)


class OcorrenciaViewsTest(TestCase):
    def setUp(self):
        # Cria usuário para teste de autenticação
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.bairro = Bairro.objects.create(nome="Santo Antônio", latitude=-9.4200, longitude=-40.5100)

    def test_dashboard_requer_login(self):
    # Verifica se usuários não autenticados são redirecionados para a tela de login
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302) # Redirect para login

    def test_dashboard_acesso_com_login(self):
    # Verifica se o dashboard carrega para usuários logados
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ocorrencias/dashboard.html')

    def test_criacao_ocorrencia(self):
    # Testa se a criação de ocorrência adiciona o registro no banco
        self.client.login(username='testuser', password='password123')
        
        data = {
            'bairro': self.bairro.id,
            'data_hora': timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
            'descricao': 'Vazamento na rede principal',
            'status': 'EM_ANDAMENTO',
            'responsavel': self.user.id
        }
        
        # Envia o formulário
        response = self.client.post(reverse('criar_ocorrencia'), data)
        
        # Redireciona para o dashboard após sucesso
        self.assertEqual(response.status_code, 302)
        
        # Confirma gravação no banco
        self.assertEqual(Ocorrencia.objects.count(), 1)