from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from account.models import Account
from rest_framework_simplejwt.tokens import RefreshToken


class VesselPermissionTests(APITestCase):
    def setUp(self):
        self.user1 = Account.objects.create_user(
            username='user1',
            email='user1@teste.com',
            password='123456'
        )
        self.user2 = Account.objects.create_user(
            username='user2',
            email='user2@teste.com',
            password='123456'
        )

        refresh = RefreshToken.for_user(self.user1)
        self.user1_token = f'Bearer {refresh.access_token}'

        refresh_user2 = RefreshToken.for_user(self.user2)
        self.user2_token = f'Bearer {refresh_user2.access_token}'

        self.client.credentials(HTTP_AUTHORIZATION=self.user1_token)
        response = self.client.post('/api/vessel/', {
            'name_vessel': 'Vessel 1',
            'capacity': 10,
            'navigation_type': 'barco'
        }, format='json')
        self.vessel1 = response.data
        self.vessel1_id = response.data.get('id') or response.data.get('pk')

    def test_criar_embarcacao_sem_autenticacao_rejeitado(self):
        """Testa que criar uma embarcação sem autenticação é rejeitado"""
        self.client.credentials()

        url = '/api/vessel/'
        response = self.client.post(url, {
            'name_vessel': 'Vessel Sem Auth',
            'capacity': 10,
            'navigation_type': 'barco'
        }, format='json')

        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_editar_embarcacao_de_outro_usuario_rejeitado(self):
        """Testa que editar a embarcação de outro usuário é rejeitado"""
        self.client.credentials(HTTP_AUTHORIZATION=self.user2_token)

        url = f'/api/vessel/{self.vessel1_id}/'
        response = self.client.patch(url, {
            'name_vessel': 'Vessel Modificada por User2'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_editar_sua_propria_embarcacao_permitido(self):
        """Testa que editar sua própria embarcação é permitido"""
        self.client.credentials(HTTP_AUTHORIZATION=self.user1_token)

        url = f'/api/vessel/{self.vessel1_id}/'
        response = self.client.patch(url, {
            'name_vessel': 'Vessel Modificada pelo Dono'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name_vessel'], 'Vessel Modificada pelo Dono')

    def test_visualizar_embarcacao_sem_autenticacao_permitido(self):
        """Testa que visualizar uma embarcação sem autenticação é permitido (público)"""

        self.client.credentials()

        url = f'/api/vessel/{self.vessel1_id}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listar_embarcacoes_sem_autenticacao_permitido(self):
        """Testa que listar embarcações sem autenticação é permitido (público)"""
        self.client.credentials()

        url = '/api/vessel/'
        response = self.client.get(url)

  
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ValidateCapacityTests(APITestCase):
    def setUp(self):
        self.user = Account.objects.create_user(
            username='teste',
            password='123456'
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_capacidade_invalida_retorna_erro(self):
        url = '/api/vessel/'

        response = self.client.post(url, {'capacity': 0}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('capacity', response.data)
