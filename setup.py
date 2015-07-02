#!/usr/bin/env python

from setuptools import setup

try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    description = open('README.md').read()

REQUIREMENTS = [i.strip() for i in open('requirements.txt').readlines()]

setup(
    name='django-rest-multitoken',
    version='0.0.0',
    packages=['multitoken'],
    license='MIT',
    author='SUNSCRAPERS',
    description='Implementation of Django Rest Framework token authentication ' +
                'that maintains multiple tokens for each user.',
    author_email='office@sunscrapers.com',
    long_description=description,
    install_requires=REQUIREMENTS,
    url='https://github.com/sunscrapers/django-rest-multitoken',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
