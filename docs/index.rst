Welcome to gorealtime-python's documentation!
=============================================

Quickstart
----------

.. code-block:: python

    import gorealtime
    client = gorealtime.Client('app_key', 'app_secret')
    client.push('Example message', ['channel1', 'second_channel'])

.. module:: gorealtime
.. autoclass:: Client

    .. automethod:: push

       :param message: string
       :param channels: list

    .. automethod:: sign

    .. automethod:: from_url
