from django.test import TestCase
from django.urls import reverse



def test_successful_collaboration_request_submission(self):
    """Test for a user requesting a collaboration"""
    post_data = {
        'name': 'test name',
        'email': 'test@email.com',
        'message': 'test message'
    }
    response = self.client.post(reverse('about'), post_data)
    self.assertEqual(response.status_code, 200)
    self.assertIn(
        b'Newsletter request received, it will be with you within 3 working days!', response.content)