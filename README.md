# Django Dynamic Email Settings

[![image](https://badge.fury.io/py/django-des.svg)](https://badge.fury.io/py/django-des) 
[![image](https://travis-ci.org/jamiecounsell/django-des.svg?branch=master)](https://travis-ci.org/jamiecounsell/django-des) [![image](https://codecov.io/gh/jamiecounsell/django-des/branch/master/graph/badge.svg)](https://codecov.io/gh/jamiecounsell/django-des)

A reusable Django application, admin panel, and EmailBackend that allows
email configuration to be changed while the server is running. The goal
of the project is to be the absolute easiest way to get email configured
across multiple
environments.

![image](https://user-images.githubusercontent.com/2321599/33807503-d7f31922-dda5-11e7-83c9-c4e7ef557cc6.png)

## Quickstart

- Install Django Dynamic Email Settings:

    ```
    $ pip install django-des
    ```

- Add it to your \`INSTALLED\_APPS\`:

    ```python
    INSTALLED_APPS = (
        ...
        'django_des',
        ...
    )
    ```

* Add the dynamic email configuration email backend to settings.py

    ```python
    EMAIL_BACKEND = 'django_des.backends.ConfiguredEmailBackend'
    ```

* To enable test email support, add Django DES's URL patterns:

    ```python
    from django_des import urls as django_des_urls


    urlpatterns = [
        ...
        url(r'^django-des/', include(django_des_urls)),
    ]
    ```

## Settings

* `DES_TEST_SUBJECT`: Set to override the default test email subject
line. (Default: `"Test Email"`)

   Example:
    
    ```python
    DES_TEST_SUBJECT = "My New Subject"
    ```

* `DES_TEST_TEXT_TEMPLATE`: Set to override the template used for text test emails. Note that this is a template file location, not a template string. (Default: `"des/test_email.txt"`)

   Example:
    
    ```python
    DES_TEST_TEXT_TEMPLATE = "myapp/email/test_email.txt"
    ```

* `DES_TEST_HTML_TEMPLATE`: Set to enable HTML emails and use the template provided as the _text/html_ content. (Default: `None`)

   Example:
    
    ```python
    DES_TEST_HTML_TEMPLATE = "myapp/email/test_email.html"
    ```


## Features

  - Configure email on the fly, no need to restart the server
  - Send test emails from the Django Admin panel
  - Test text and HTML email sending
  - Supports third party mail packages like
    [django-mailer](https://github.com/pinax/django-mailer)

## Support

**Python**

  - 2.7
  - 3.4
  - 3.5
  - 3.6

**Django**

  - 1.8
  - 1.9
  - 1.10
  - 1.11
  - 2.0

## Running Tests

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_dev.txt
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ tox

## Credits

Tools used in rendering this
    package:

  - [Cookiecutter](https://github.com/audreyr/cookiecutter)
  - [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage)
