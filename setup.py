from setuptools import setup, find_packages
 
version = '0.1.2'
 
LONG_DESCRIPTION = """
django-memcached
=================

This is a very simple reusable app which does one thing: shows you statistics
about your currently running memcached instances.  There are no database models
and not much configuration.

Installing django-memcached
----------------------------

1. Either download the tarball and run ``python setup.py install``, or simply
   use easy install or pip like so ``easy_install django-memcached``.


2. Add django_memcached to your ``INSTALLED_APPS`` setting::

       INSTALLED_APPS = (
           # ...
           'django_memcached',
       )


3. Add the urls to your url configuration::

       urlpatterns = patterns('',
           # ...
           (r'^cache/', include('django_memcached.urls')),
       )


4. If you want to restrict these urls to only staff members, just add this
   setting to your settings file::
   
       DJANGO_MEMCACHED_REQUIRE_STAFF = True


That's it.  Hopefully this app gives you a little insight into how your
memcached servers are being utilized.
"""
 
setup(
    name='django-memcached',
    version=version,
    description="django-memcached is a very simple reusable app which does one simple thing: shows you statistics about your currently running memcached instances",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='memcached,django',
    author='Eric Florenzano',
    author_email='floguy@gmail.com',
    url='http://github.com/ericflo/django-memcached/tree/master',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools'],
    include_package_data=True,
    setup_requires=['setuptools_git'],
)