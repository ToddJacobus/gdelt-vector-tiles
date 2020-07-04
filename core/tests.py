from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

import mapbox_vector_tile

from core.models import Point

def sample_point(**params):
    """Create and return a sample polygon"""
    defaults = {
        'geometry': 'POINT (0 0)'
    }
    defaults.update(params)

    return Point.objects.create(**defaults)

def mvt_url(zoom, x, y):
    return reverse('core:mvt_tiles', args=[zoom, x, y])

class PublicTileApiTests(TestCase):
    """A suite of public api tests for the tile api"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_valid_tiles(self):
        point = sample_point()
        url = mvt_url(0, 0, 0)
        
        res = self.client.get(url) 

        decoded_data = mapbox_vector_tile.decode(res.content)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(decoded_data)
              
