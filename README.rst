=============================
Django Dynamic Email Settings
=============================

.. image:: https://badge.fury.io/py/django-des.svg
    :target: https://badge.fury.io/py/django-des

.. image:: https://travis-ci.org/jamiecounsell/django-des.svg?branch=master
    :target: https://travis-ci.org/jamiecounsell/django-des

.. image:: https://codecov.io/gh/jamiecounsell/django-des/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/jamiecounsell/django-des

A reusable Django application and EmailBackend that allows email configuration to be changed while the server is running.

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

Features
--------

* TODO

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
