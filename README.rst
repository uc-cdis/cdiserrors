Auth Errors to be used by the auth systems that might be used in Gen3 services.


Installation
------------

.. code-block:: console

    $ pip install cdiserrors

or

.. code-block:: console

    $ poetry add cdiserrors


Flask Support
`````````````

This provides:

* ``cdiserrors.make_json_error(ex: Exception) -> Response``
* ``cdiserrors.setup_default_handlers(app: Flask)``

.. code-block:: console

    $ pip install cdiserrors[flask]

or

.. code-block:: console

    $ poetry add cdiserrors -E flask
