from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from client_api.models import ClientEntity, Request


class ClientListCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_clients(self):
        response = self.client.get(reverse('client_list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_client(self):
        data = {
            'first_name': 'Rick',
            'last_name': 'Sanchez',
            'phone': 1233445137
        }
        response = self.client.post(reverse('client_list_create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ClientEntity.objects.count(), 1)
        self.assertEqual(ClientEntity.objects.get().first_name, 'Rick')


class ClientGetUpdateDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client_entity = ClientEntity.objects.create(first_name='Morty', last_name='Smith', phone=3454665788)
        self.client_entity.save()

    def test_get_client(self):
        response = self.client.get(reverse('handle_client', args=[self.client_entity.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_client(self):
        data = {
            'first_name': 'Morty',
            'last_name': 'Chauncey',
            'phone': 3454665788
        }
        response = self.client.put(reverse('handle_client', args=[self.client_entity.id]), data=data,
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ClientEntity.objects.get(id=self.client_entity.id).last_name, 'Chauncey')

    def test_delete_client(self):
        response = self.client.delete(reverse('handle_client', args=[self.client_entity.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ClientEntity.objects.count(), 0)

    def test_get_invalid_client(self):
        response = self.client.get(reverse('handle_client', args=[self.client_entity.id + 1]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class RequestListCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client_entity = ClientEntity.objects.create(first_name='Morty', last_name='Smith', phone=3454665788)
        self.client_entity.save()
        self.request = Request.objects.create(client=self.client_entity, body="Sample request 1")

    def test_get_requests(self):
        response = self.client.get(reverse('request_list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_request(self):
        data = {
            'client': 1,
            'body': 'Sample request 2',
        }
        response = self.client.post(reverse('request_list_create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'A request from Morty Smith was created successfully.')
        self.assertEqual(response.data['data']['status'], 'Pending')
