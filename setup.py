from distutils.core import setup
import django_oopviews

setup(
        name="django-oopviews",
        author="Horst Gutmann",
        author_email="zerok@zerokspot.com",
        packages=['django_oopviews'],
        url="http://github.com/zerok/django-oopviews/",
        version=django_oopviews.get_version(),
        description="django-oopviews provides a simple way to write Django-views in an object-oriented manner.",
        license="BSD",
        platforms=['any'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developer',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ]
        )
