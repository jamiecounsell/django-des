=====
Usage
=====

To use Django Dynamic Email Settings in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_des.apps.DjangoDesConfig',
        ...
    )

Add Django Dynamic Email Settings's URL patterns:

.. code-block:: python

    from django_des import urls as django_des_urls


    urlpatterns = [
        ...
        url(r'^', include(django_des_urls)),
        ...
    ]
