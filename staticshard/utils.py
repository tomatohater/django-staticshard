# -*- coding: utf-8 -*-
"""
Utility methods django-staticshard.
"""
import hashlib
from urlparse import urljoin, urlparse, urlunparse

from django.core.exceptions import ImproperlyConfigured

from .settings import STATICSHARD_CACHE, STATICSHARD_HOSTS


def check_settings():
    """
    Checks if the staticshard settings have sane values.
    """
    if not STATICSHARD_HOSTS:
        raise ImproperlyConfigured(
            "You're using the staticshard app "
            "without having set the required STATICSHARD_HOSTS setting.")


def get_absolute_url(resource_url):
    """
    Get the fully qualified domain-sharded url.
    """
    parts = urlparse(resource_url)
    shard = get_shard(parts.path)
    if parts.netloc:
        return resource_url.replace(parts.netloc, shard)
    else:
        parts_dict = parts._asdict()
        parts_dict['scheme'] = 'http'
        parts_dict['netloc'] = shard
        return urlunparse(parts_dict.values())


def get_shard(resource_url):
    """
    Get the domain shard for a given resource url.
    """
    check_settings()
    md5 = hashlib.md5()
    md5.update(resource_url)
    shard_index = int(md5.hexdigest(), 16) % len(STATICSHARD_HOSTS)
    return STATICSHARD_HOSTS[shard_index]
