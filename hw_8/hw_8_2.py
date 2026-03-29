""" Homework 8 task 2 """


import unittest
from unittest.mock import patch, Mock
import requests


class WebService:
    """Class my web service"""
    def get_data(self, url: str) -> dict:
        """Get data from url request"""
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Request failed with status code {response.status_code}")


class TestWebService(unittest.TestCase):
    """Class Test for web service"""
    def setUp(self):
        self.service = WebService()

    @patch("requests.get")
    def test_get_data_success(self, mock_get):
        """Test get data success. Creating a fake response"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}

        mock_get.return_value = mock_response

        result = self.service.get_data("http://some-url.com")

        self.assertEqual(result, {"data": "test"})
        mock_get.assert_called_once_with("http://some-url.com")

    @patch("requests.get")
    def test_get_data_404(self, mock_get):
        """Test get data failure. Fake answer with error"""
        mock_response = Mock()
        mock_response.status_code = 404

        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            self.service.get_data("http://some-url.com")

        self.assertIn("404", str(context.exception))

    @patch("requests.get")
    def test_get_data_500(self, mock_get):
        """Test get data failure. Other server error"""
        mock_response = Mock()
        mock_response.status_code = 500

        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            self.service.get_data("http://some-url.com")

        self.assertIn("500", str(context.exception))


if __name__ == "__main__":
    unittest.main()
