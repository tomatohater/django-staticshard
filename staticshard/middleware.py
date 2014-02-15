import re

from django.conf import settings

from .utils import get_absolute_url


class StaticShardMiddleware(object):
    """Beefs up the Cache-Control HTTP header. Appends 'no-cache, no-store'
    when response should not be cached.
    """
    def process_response(self, request, response):

        regex = re.compile("(https?://[^'\"<]*)",re.IGNORECASE|re.MULTILINE)

        for i, content in enumerate(response._container):
            changed = False
            urls = regex.findall(content)
            for url in urls:
                if settings.STATIC_URL in url:
                    content = content.replace(url, get_absolute_url(url))
                    changed = True
            if changed:
                response._container[i] = content
        return response
