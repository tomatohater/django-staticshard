from django import template
from django.template.base import Node
from django.templatetags.static import StaticNode
from django.utils.encoding import iri_to_uri
from django.utils.six.moves.urllib.parse import urljoin

from ..utils import get_absolute_url

register = template.Library()


class StaticShardNode(StaticNode):
    """
    Extends django's static tag with domain sharding.
    """
    def url(self, context):
        """
        Get's the domain sharded url.
        """
        url = super(StaticShardNode, self).url(context)
        return get_absolute_url(url)

    @classmethod
    def handle_simple(cls, path):
        """
        Get's the domain sharded url.
        """
        url = super(StaticShardNode, cls).handle_simple(path)
        return get_absolute_url(url)


@register.tag('staticshard')
def do_staticshard(parser, token):
    """
    Joins the given path with the sharded domain.

    Usage::

        {% staticshard path [as varname] %}

    Examples::

        {% staticshard "myapp/css/base.css" %}
        {% staticshard variable_with_path %}
        {% staticshard "myapp/css/base.css" as admin_base_css %}
        {% staticshard variable_with_path as varname %}

    """
    return StaticShardNode.handle_token(parser, token)


def staticshard(path):
    return StaticShardNode.handle_simple(path)