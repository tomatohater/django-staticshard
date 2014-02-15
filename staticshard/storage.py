# -*- coding: utf-8 -*-
"""A Django storage backend that returns sharded domains."""

from django.contrib.staticfiles.storage import StaticFilesStorage

from .settings import STATICSHARD_HOSTS
from .utils import check_settings, get_absolute_url


class StaticShardFilesStorage(StaticFilesStorage):
    """
    Extends standard StaticFilesStorage to support domain sharding.
    """
    def __init__(self, *args, **kwargs):
        check_settings()
        super(StaticShardFilesStorage, self).__init__(*args, **kwargs)

    def url(self, name):
        original_url = super(StaticShardFilesStorage, self).url(name)
        return get_absolute_url(original_url)