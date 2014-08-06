# -*- coding: utf-8 -*-

import os
import sys


project_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(project_dir, 'src'))

import django_bootstrap_carousel

version = django_bootstrap_carousel.version

install_requires = [
    'django',
]

setup_requires = [
]

dependency_links = [
]

long_description = '''
django-bootstrap-carousel implement the carousel component for
bootstrap in Django. See the project page for more information:
https://github.com/cdchen/django-bootstrap-carousel

'''

from setuptools import setup, find_packages

setup(
    name='django_bootstrap_carousel',
    version=version,
    description='Django Bootstrap Carousel Component',
    long_description=long_description,
    author='cdchen',
    author_email='cdchen@nicestudio.com.tw',
    url='https://github.com/cdchen/django-bootstrap-carousel',
    download_url='https://github.com/cdchen/django-bootstrap-carousel',
    license='MIT License',
    packages=find_packages('src', exclude=['docs', 'tests']),
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    classifiers=['Classifier: Development Status :: 4 - Beta',
                 'Classifier: Development Status :: 5 - Production/Stable',
                 'Classifier: Environment :: Web Environment',
                 'Classifier: Framework :: Django',
                 'Classifier: Intended Audience :: Developers',
                 'Classifier: License :: OSI Approved :: MIT License',
                 'Classifier: Operating System :: OS Independent',
                 'Classifier: Programming Language :: Python',
                 'Classifier: Programming Language :: Python :: 3',
                 'Classifier: Topic :: Utilities'],
)
