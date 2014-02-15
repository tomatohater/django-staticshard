# -*- coding: utf-8 -*-
"""
Default settings for package (overridable with Django settings).
"""

from django.conf import settings


#
# Specify a cache name. Defaults 'default'.
#
STATICSHARD_CACHE = getattr(settings, 'STATICSHARD_CACHE', 'default')

#
# Specify the hostnames of the domain shards. Defaults to empty tuple.
#
STATICSHARD_HOSTS = getattr(settings, 'STATICSHARD_HOSTS', ())


