# -*- coding: utf-8 -*-

import os
import sys


version = '0.1'

install_requires = [
    'lettuce',
    'django',
    'django-libs',
    'django-extensions',
    'django-model-utils',
    'django-nose',
]

setup_requires = [
]

dependency_links = [
]

long_description = '''

'''

from setuptools import setup, find_packages

setup(
    name='django_bootstrap_carousel',
    version=version,
    description="",
    long_description=long_description,
    author='cdchen',
    author_email='cdchen@nicestudio.com.tw',
    url='http://www.nicestudio.com.tw/projects/django_bootstrap_carousel',
    license='',
    packages=find_packages('src', exclude=['docs', 'tests']),
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
)

# End of file.
