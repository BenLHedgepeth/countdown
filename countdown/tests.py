
from unittest.mock import Mock, patch
from django.test import TestCase
from django.urls import reverse

import requests

class TestCountdownPage(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.data = {
            'regionName': "Wilsonville",
            'state': "Oregon"
        }

    def test_ip_address_physical_location(self):
        '''Verify that a city and state are returned
        when an IP Address is facilitated'''

        with patch.object(requests, 'get', return_value=self.data) as mock_get:
            response = self.client.get(reverse(""))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed("countdown.html")
            self.assertContains("Wilsonville")
