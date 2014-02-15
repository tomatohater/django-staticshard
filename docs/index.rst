django-staticshard
==================

Domain sharding for Django static files.

.. image:: https://travis-ci.org/tomatohater/django-staticshard.png?branch=master
    :target: https://travis-ci.org/tomatohater/django-staticshard

.. image:: https://coveralls.io/repos/tomatohater/django-staticshard/badge.png?branch=master
    :target: https://coveralls.io/r/tomatohater/django-staticshard?branch=master

.. image:: https://badge.fury.io/py/django-staticshard.png
    :target: http://badge.fury.io/py/django-staticshard

``django-staticshard`` provides a set of utilities which to easily enable domain sharding of static files in your Django project?


What is Domain Sharding?
************************

Domain sharding is a technique used to accerate the time it takes for a webpage to render in a browser. Web browsers will only open a small number of parallel connections to each domain (~2-16). The theory is that if your webpage contains a lot of external assets from a single domain, you may experience a bottleneck while the browser wait for files to download before making the next request. Spreading these requests across multiple domains will allow more files to be downloaded in parallel, thus accelerating the page render time. Of course, each new domain incur the cost of a DNS lookup... so there is a balance to be struck.

Read what Google has to say about it.
https://developers.google.com/speed/pagespeed/service/ShardResources


Why are you doing this?
***********************

Domain sharding is a science, not an art. But there is reliable no formula for it. In certain cases it has no impact on page speed. In others, the effects may be significant. In addition, determining the ideal number of domains needs to take into account a variety of factors. 
In order to determine whether sharding even makes sense, it would be helpful

I felt that in order to make informed decisions about domain sharding, one must able to easily test it's impact in multiple configurations. So a tool that makes it easy to implement domain sharding is desirable. 



Read The Docs
*************

https://django-staticshard.readthedocs.org/en/latest/