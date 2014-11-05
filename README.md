# spate-python [![Build Status](https://travis-ci.org/spateio/spate-python.svg)](https://travis-ci.org/spateio/spate-python) [![Coverage Status](https://coveralls.io/repos/spateio/spate-python/badge.png)](https://coveralls.io/r/spateio/spate-python)

## Quickstart

```python

    import spate
    client = spate.Spate('app_key', 'app_secret')
    client.push('Example message', ['channel1', 'second_channel'])
```

## Installation

Installation is done using `pip`

`$ pip install spate`

If you want the latest possible version, grab it directly from the git repo.
However, be careful as this *may be broken*.

`$ pip install git+https://github.com/spateio/spate-python.git`

# Links
- [Docs](http://spate-python.readthedocs.org/en/latest/)
- [Issues](https://github.com/spateio/spate-python/issues)
- [CI](https://travis-ci.org/spateio/spate-python)
