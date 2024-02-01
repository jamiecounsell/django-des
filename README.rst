Django Dynamic Email Settings
=============================

|image1| |image2| |image3| |image4|

A reusable Django application, admin panel, and EmailBackend that allows
email configuration to be changed while the server is running. The goal
of the project is to be the absolute easiest way to get email configured
across multiple environments.

|image5|

Quickstart
----------

-  Install Django Dynamic Email Settings:

   ::

       $ pip install django-des

-  Add it to your \`INSTALLED_APPS`:

   .. code:: python

       INSTALLED_APPS = (
           ...
           'des',
           ...
       )

-  Add the dynamic email configuration email backend to settings.py

   .. code:: python

       EMAIL_BACKEND = 'des.backends.ConfiguredEmailBackend'

-  Run ``manage.py migrate des``

-  To enable test email support, add Django DES's URL patterns:

   .. code:: python

       from des import urls as des_urls


       urlpatterns = [
           ...
           url(r'^django-des/', include(des_urls)),
       ]

Settings
--------

-  ``DES_TEST_SUBJECT``: Set to override the default test email subject
   line. (Default: ``"Test Email"``)

   Example:

   .. code:: python

       DES_TEST_SUBJECT = "My New Subject"

-  ``DES_TEST_TEXT_TEMPLATE``: Set to override the template used for
   text test emails. Note that this is a template file location, not a
   template string. (Default: ``"des/test_email.txt"``)

   Example:

   .. code:: python

       DES_TEST_TEXT_TEMPLATE = "myapp/email/test_email.txt"

-  ``DES_TEST_HTML_TEMPLATE``: Set to enable HTML emails and use the
   template provided as the *text/html* content. (Default: ``None``)

   Example:

   .. code:: python

       DES_TEST_HTML_TEMPLATE = "myapp/email/test_email.html"

Features
--------

-  Configure email on the fly, no need to restart the server
-  Send test emails from the Django Admin panel
-  Test text and HTML email sending
-  Supports third party mail packages like `django-mailer`_

Support
-------

**Python**

-  3.6
-  3.7
-  3.8
-  3.9
-  3.10
-  3.11

**Django**

-  3.2
-  4.0
-  5.0

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

-  `Cookiecutter`_
-  `cookiecutter-djangopackage`_

.. _django-mailer: https://github.com/pinax/django-mailer
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-djangopackage: https://github.com/pydanny/cookiecutter-djangopackage

.. |image1| image:: https://img.shields.io/pypi/v/django-des.svg
   :target: https://pypi.python.org/pypi/django-des
.. |image2| image:: https://img.shields.io/travis/jamiecounsell/django-des.svg
   :target: https://travis-ci.org/jamiecounsell/django-des
.. |image3| image:: https://img.shields.io/codecov/c/github/jamiecounsell/django-des.svg
   :target: https://codecov.io/gh/jamiecounsell/django-des
.. |image4| image:: https://img.shields.io/pypi/l/django-des.svg
   :target: https://github.com/jamiecounsell/django-des/blob/master/LICENSE
.. |image5| image:: https://user-images.githubusercontent.com/2321599/33807503-d7f31922-dda5-11e7-83c9-c4e7ef557cc6.png
