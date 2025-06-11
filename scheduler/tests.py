from django.test import TestCase
from unittest.mock import patch
from passage.models import City, Passage
from user.models import User
from scheduler.services import genera_micro_program_seaman

class OpenRouterIntegrationTest(TestCase):
    @patch('scheduler.services.requests.post')
    def test_genera_micro_program_seaman(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "choices": [
                {"message": {"content": "Roteiro de teste para 7 dias."}}
            ]
        }
        cidade = City.objects.create(name="Manaus")
        passage = Passage.objects.create(
            origin=cidade,
            destination=cidade,
            travel_date="2024-07-01",
            arrival_date="2024-07-02"
        )
        user = User.objects.create(username="teste")
        result = genera_micro_program_seaman(passage, user)
        print(result)
        self.assertEqual(result, "Roteiro de teste para 7 dias.")