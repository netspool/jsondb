"""
jsonDB
--------

jsonDB is lightweight, fast, and simple database based on Python's own
json module. And it's BSD licensed!

jsonDB is Fun
```````````````

::

    >>> import jsondb

    >>> db = jsondb.load('test.db', False)

    >>> db.set('key', 'value')

    >>> db.get('key')
    'value'

    >>> db.dump()
    True


And Easy to Install
```````````````````

::

    $ pip install jsondb

Links
`````

* `website <http://packages.python.org/jsonDB/>`_
* `documentation <http://packages.python.org/jsonDB/commands.html>`_
* `bitbucket repo <https://bitbucket.org/patx/jsondb>`_

"""

from distutils.core import setup

setup(name = "jsonDB",
    version="0.1.0",
    description="A lightweight and simple database using ujson.",
    author="Harrison Erd / Dainis Karakulko",
    author_email="dennis.karakulko@gmail.com",
    license="three-clause BSD",
    url="https://github.com/netspool/jsondb",
    long_description=__doc__,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Topic :: Database" ],
    py_modules=['jsondb'],
    install_requires=['ujson'])
