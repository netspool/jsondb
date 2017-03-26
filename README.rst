jsonDB
--------

jsonDB is lightweight, fast, and simple database based on the `ujson <https://pypi.python.org/pypi/ujson/>`_ module. And it's BSD licensed!


jsonDB is Fun
```````````````

    >>> import jsondb

    >>> db = jsondb.load('test.db', False)

    >>> db.set('key', 'value')

    >>> db.get('key')
    'value'

    >>> db.dump()
    True


Easy to Install
```````````````

    $ pip install jsondb


Links
`````

* `website <http://packages.python.org/jsonDB/>`_
* `documentation <http://packages.python.org/jsonDB/commands.html>`_
* `pypi
  <http://pypi.python.org/pypi/jsonDB>`_
