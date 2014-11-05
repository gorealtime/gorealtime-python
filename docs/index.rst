Welcome to spate-python's documentation!
=============================================

Quickstart
----------

Installation
^^^^^^^^^^^^^

Installation is done using `pip`

.. code-block:: bash

    $ pip install spate

If you want the latest possible version, grab it directly from the git repo.
However, be careful as this *may be broken*.

.. code-block:: bash

    $ pip install git+https://github.com/spateio/spate-python.git


Usage
^^^^^^^

.. code-block:: python

    import spate
    client = spate.Spate('app_key', 'app_secret')
    client.push('Example message', ['channel1', 'second_channel'])

.. module:: spate
.. autoclass:: Spate

    .. automethod:: push

       :param message: string
       :param channels: list

    .. automethod:: sign

    .. automethod:: from_url
