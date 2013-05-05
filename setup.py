#!/usr/bin/python
from setuptools import setup
from setuptools import find_packages

long_desc = open('README.md').read()

setup(
    name='django-columninline',
    version='0.1',
    description='Django ColumnInline',
    packages=find_packages(),
    long_description=long_desc,
    url='https://github.com/DjangoAdminHackers/ColumnInline',
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)