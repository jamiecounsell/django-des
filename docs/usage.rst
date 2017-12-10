=====
Usage
=====

To use Django Dynamic Email Settings in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'des.apps.DjangoDesConfig',
        ...
    )

Add Django Dynamic Email Settings's URL patterns:

.. code-block:: python

    from des import urls as des_urls


    urlpatterns = [
        ...
        url(r'^', include(des_urls)),
        ...
    ]
