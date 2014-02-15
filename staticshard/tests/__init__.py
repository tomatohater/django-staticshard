# -*- coding: utf-8 -*-
"""
Test suite for django-staticshard.
"""
import uuid
from urlparse import urlparse

from django.conf import settings
from django.test import TestCase
from django.core.exceptions import ImproperlyConfigured

from ..settings import STATICSHARD_HOSTS
from ..utils import get_absolute_url


class StaticShardTests(TestCase):
    """Test case for django-staticshard."""
   
    resources = ['img/%s.jpg' % uuid.uuid4() for i in range(0, 20)]

    def test_absolute_url(self):
        """
        Test the absolute_url method.
        """
        for resource in self.resources:
            urls = []
            for i in range(0, 5):
                url = get_absolute_url(resource)
                self.assertNotIn(settings.STATIC_URL, url)
                parts = urlparse(url)
                self.assertIn(parts.netloc, STATICSHARD_HOSTS)
                urls.append(url)
            self.assertEqual(urls[0], urls[1])
            self.assertEqual(urls[0], urls[2])
            self.assertEqual(urls[0], urls[3])
            self.assertEqual(urls[0], urls[4])
    