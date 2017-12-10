=============================
Django Dynamic Email Settings
=============================

.. image:: https://badge.fury.io/py/django-des.svg
    :target: https://badge.fury.io/py/django-des

.. image:: https://travis-ci.org/jamiecounsell/django-des.svg?branch=master
    :target: https://travis-ci.org/jamiecounsell/django-des

.. image:: https://codecov.io/gh/jamiecounsell/django-des/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jamiecounsell/django-des

A reusable Django application, admin panel, and EmailBackend that allows email configuration to be changed while the server is running. The goal of the project is to be the absolute easiest way to get email configured across multiple environments.

.. image:: https://user-images.githubusercontent.com/2321599/33801548-635ffd42-dd2c-11e7-8a44-162969f2ee36.png


Documentation
-------------

The full documentation is at https://django-des.readthedocs.io.

Quickstart
----------

Install Django Dynamic Email Settings::

    pip install django-des

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_des',
        ...
    )

Add the dynamic email configuration email backend to `settings.py`

.. code-block:: python


    EMAIL_BACKEND = 'django_des.backends.ConfiguredEmailBackend'


To enable test email support, add Django DES's URL patterns:

.. code-block:: python

    from django_des import urls as django_des_urls


    urlpatterns = [
        ...
        url(r'^django-des/', include(django_des_urls)),
    ]


Features
--------

* Configure email on the fly, no need to restart the server
* Send test emails from the Django Admin panel
* Test text and HTML email sending
* Supports third party mail packages like `django-mailer <https://github.com/pinax/django-mailer>`_



Support
-------------

**Python**

* 2.7
* 3.4
* 3.5
* 3.6

**Django**

* 1.8
* 1.9
* 1.10
* 1.11
* 2.0

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_dev.txt
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
