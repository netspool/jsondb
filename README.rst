ujsonDB
--------

ujsonDB is lightweight, fast, and simple database based on the `ujson <https://pypi.python.org/pypi/ujson/>`_ module.


```````````````

    >>> import ujsondb

    >>> db = ujsondb.load('test.db', False)

    >>> db.set('key', 'value')

    >>> db.get('key')
    'value'

    >>> db.dump()
    True


Easy to Install
```````````````

    $ pip install ujsondb
