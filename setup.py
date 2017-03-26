"""
ujsonDB
--------

ujsonDB is lightweight, fast, and simple database based on Python's own
json module. And it's BSD licensed!

ujsonDB is Fun
```````````````

::

    >>> import ujsondb

    >>> db = jsondb.load('test.db', False)

    >>> db.set('key', 'value')

    >>> db.get('key')
    'value'

    >>> db.dump()
    True


And Easy to Install
```````````````````

::

    $ pip install ujsondb

Links
`````

* `website <http://packages.python.org/ujsonDB/>`_
* `documentation <http://packages.python.org/ujsonDB/commands.html>`_

"""

from distutils.core import setup

setup(name = "ujsonDB",
    version="0.1.0",
    description="A lightweight and simple database using ujson.",
    author="Harrison Erd / Dainis Karakulko",
    author_email="dennis.karakulko@gmail.com",
    license="three-clause BSD",
    url="https://github.com/netspool/ujsondb",
    long_description=__doc__,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Topic :: Database" ],
    py_modules=['ujsondb'],
    install_requires=['ujson'])
