from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
import django_oopviews

setup(
        name="django-oopviews",
        author="Horst Gutmann",
        author_email="zerok@zerokspot.com",
        packages=find_packages(),
        url="http://github.com/zerok/django-oopviews/",
        version=django_oopviews.get_version(),
        description="django-oopviews provides a simple way to write Django-views in an object-oriented manner.",
        license="BSD",
        platforms=['any'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ]
        )
