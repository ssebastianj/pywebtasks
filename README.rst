PyWebtasks: A Python wrapper for Auth0's Webtasks API
=====================================================

.. image:: https://img.shields.io/pypi/v/pywebtasks.svg
    :target: https://pypi.python.org/pypi/pywebtasks

.. image:: https://img.shields.io/pypi/dm/pywebtasks.svg
        :target: https://pypi.python.org/pypi/pywebtasks

.. image:: http://img.shields.io/travis/ssebastianj/pywebtasks.png
   :target: https://travis-ci.org/ssebastianj/pywebtasks



Installation
------------
To install PyWebtasks, simply:

.. code-block:: bash

    $ pip install pywebtasks

Usage
-----
Create a new webtask token:

.. code-block:: python

    >>> from pywebtasks import tokens
    >>> wt_token = tokens.create('your_auth_webtask_token')

To view your user's auth webtask token go to the `webtask.io token section <https://webtask.io/token>`_.

To revoke a webtask token:

.. code-block:: python

    >>> tokens.revoke(wt_token)

Run a webtask from a string:

.. code-block:: python

    >>> import pywebtasks
    >>> js_code = '''return function (context, cb) {
                       cb(null, "Hello, JS world!");
                     };
                  '''
    >>> req = pywebtasks.run(js_code,
                             'a_wt_container_name-0',
                             'a_webtask_token')
    >>> req.content
    'Hello, JS world!'


If you want to run the content of a source code file (for example, `javascript.js </test_code/javascript.js>`_), you can use the ``run_file`` function:

.. code-block:: python

    >>> req = pywebtasks.run_file('/path/to/a/file.js',
                                  'a_wt_container_name-0',
                                  'a_webtask_token')
    >>> req.content
    'Hello, JS world!'
