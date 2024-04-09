from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch


class GetDatasetsTests(APITestCase):

    @patch('collections_api.views.requests.get')
    def test_get_datasets_without_pub_key(self, mock_get):
        url = reverse('get_datasets')  # Ensure your URL name matches the name in your urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(response.data, {'error': 'Parameter "pub_key" is required'})

    @patch('collections_api.views.requests.get')
    def test_get_datasets_with_pub_key_success(self, mock_get):
        # Mock the external API call to return a successful response
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'results': [{'dataset_key': '123'}]}
        url = reverse('get_datasets') + '?pub_key=66522820-055c-11d8-b84e-b8a03c50a862'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, {'publications': [{'dataset_key': '123'}]})

    @patch('collections_api.views.requests.get')
    def test_get_datasets_with_pub_key_failure(self, mock_get):
        # Simulate an API failure with a 500 response
        mock_response = mock_get.return_value
        mock_response.status_code = 500
        url = reverse('get_datasets') + '?pub_key=66522820-055c-11d8-b84e-b8a03c50a862'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertDictEqual(response.data, {'error': 'Failed to fetch data from GBIF'})

class GetPublicationsTests(APITestCase):

    @patch('collections_api.views.requests.get')
    def test_get_publications_missing_parameters(self, mock_get):
        # Test the scenario where required parameters are missing
        url = reverse('get_publications')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(response.data, {'error': 'Parameter "pub_key" is required'})

        # Now test missing just the dataset_key
        url += '?pub_key=66522820-055c-11d8-b84e-b8a03c50a862'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(response.data, {'error': 'Parameter "dataset_key" is required'})

    @patch('collections_api.views.requests.get')
    def test_get_publications_success(self, mock_get):
        # Simulate a successful API call for fetching publications
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None  # Assume no exceptions
        mock_response.status_code = 200
        mock_response.json.return_value = {'results': [{'title': 'Test Publication'}]}
        url = reverse('get_publications') + '?pub_key=66522820-055c-11d8-b84e-b8a03c50a862&dataset_key=f934f8e2-32ca-46a7-b2f8-b032a4740454'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['publications'][0]['title'], 'Test Publication')

    @patch('collections_api.views.requests.get')
    def test_get_publications_gbif_api_error(self, mock_get):
        # Test the handling of a simulated GBIF API error
        mock_get.side_effect = Exception("GBIF API error")
        url = reverse('get_publications') + '?pub_key=66522820-055c-11d8-b84e-b8a03c50a862&dataset_key=f934f8e2-32ca-46a7-b2f8-b032a474045'
