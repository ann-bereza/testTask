from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from client_api.models import Request, ClientEntity


class RequestViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.request_client = ClientEntity()
        self.request_client.save()
        self.request = Request.objects.create(client=self.request_client, body="Sample request 1", status="Pending")

    def test_get_request(self):
        url = reverse('handle_request', args=[self.request.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['body'], 'Sample request 1')

    def test_update_request(self):
        data = {'body': 'Updated Request', 'status': 'Completed'}
        url = reverse('handle_request', args=[self.request.id])
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Request information has been updated successfully.')
        self.assertEqual(response.data['data']['status'], 'Completed')

    def test_delete_request(self):
        response = self.client.delete(reverse('handle_request', args=[self.request.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Request.objects.filter(id=self.request.id).exists())
