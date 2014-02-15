from setuptools import setup, find_packages
import os

import staticshard


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')

setup(
    name='django-staticshard',
    version=staticshard.__version__,
    description='Domain sharding for Django static files.',
    long_description=README,
    url='https://github.com/tomatohater/django-staticshard',
    author='Drew Engelson',
    author_email='drew@engelson.net',
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    package_data={},
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
