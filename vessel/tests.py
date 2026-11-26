from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from account.models import Account
from rest_framework_simplejwt.tokens import RefreshToken

class ValidateCapacityTests(APITestCase):
    def setUp(self):
        # Create a test user and get JWT token
        self.user = Account.objects.create_user(
            username='igor.leite',
            password='123456'
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_capacidade_invalida_retorna_erro(self):
        url = '/api/vessel/'

        response = self.client.post(url, {'capacity': 0}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # A resposta contém erros de validação dos campos obrigatórios e capacity
        self.assertIn('capacity', response.data)
