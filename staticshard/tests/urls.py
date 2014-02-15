# -*- coding: utf-8 -*-
"""Url handlers for tests."""

try:
    from django.conf.urls import patterns
except ImportError:
    # For Django versions older than 1.4 (removed in 1.6)
    from django.conf.urls.defaults import patterns


urlpatterns = patterns('django.views.generic.simple',
    (r'^test-static/$', 'direct_to_template', {'template': 'static.html'}),
    (r'^test-templatetag/$', 'direct_to_template', {'template': 'templatetag.html'}),
    (r'^test-middleware/$', 'direct_to_template', {'template': 'middleware.html'}),
)
