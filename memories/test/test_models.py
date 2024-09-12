# memories/test/test_models.py

from rest_framework import status
from rest_framework.test import APITestCase


class MemoryAPITestCase(APITestCase):

    def setUp(self):
        self.url = '/api/memories/'

    def test_memory_api_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_memory_api_post(self):
        data = {
            'title': 'Test Memory',
            'description': 'Test Description',
            'photo': None,
            'video': None,
            'document': None,
            'link': ''
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
