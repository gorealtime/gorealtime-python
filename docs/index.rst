Welcome to spate-python's documentation!
=============================================

Quickstart
----------

.. code-block:: python

    import spate
    client = spate.Client('app_key', 'app_secret')
    client.push('Example message', ['channel1', 'second_channel'])

.. module:: spate
.. autoclass:: Client

    .. automethod:: push

       :param message: string
       :param channels: list

    .. automethod:: sign

    .. automethod:: from_url
