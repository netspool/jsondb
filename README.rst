ujsonDB
--------

ujsonDB is lightweight, fast, and simple database based on the `ujson <https://pypi.python.org/pypi/ujson/>`_ module. And it's BSD licensed!


ujsonDB is Fun
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

    $ pip install jusondb


Links
`````

* `website <http://packages.python.org/ujsonDB/>`_
* `documentation <http://packages.python.org/ujsonDB/commands.html>`_
* `pypi
  <http://pypi.python.org/pypi/ujsonDB>`_
