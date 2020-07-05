from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Point
from point.serializers import PointSerializer


POINT_URL = reverse('point:point-list')

def sample_point(**params):
    """create and return a sample point"""
    defaults = {
        'geometry': 'POINT (30 10)',
    }
    defaults.update(params)

    return Point.objects.create(**defaults)


class PublicPointAPITests(TestCase):
    """A suite of tests for the public point API"""
    def setUp(self):
        self.client = APIClient()

    def test_create_point(self):
        """Test that a point can be created"""
        payload = {
            'geometry': 'POINT (10 12)'
        }
        res = self.client.post(POINT_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)