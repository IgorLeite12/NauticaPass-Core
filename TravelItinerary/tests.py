from django.test import TestCase
from django.urls import reverse

class RoteiroViewTest(TestCase):
    def test_gerar_roteiro(self):
        url = reverse('gerar-roteiro')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 200)
        self.assertIn('resposta', response.json())