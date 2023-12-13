Installation
============

Installing for usage
--------------------

.. mdinclude:: ../README.md
   :start-line: 22
   :end-line: 27

Installing for development
--------------------------

First, you need to get the sources.

.. code-block:: bash

   git clone git@github.com:2Fake/ssllabs.git

Then you need to take care of the requirements. Please take care of creating a virtual environment if needed.

.. code-block:: bash

   cd ssllabs
   python -m pip install -e .[dev]

This will also install a pre-commit environment for you. To install the git hook scripts, run:

.. code-block:: bash

   pre-commit install

Testing
-------

.. mdinclude:: ../tests/README.md
   :start-line: 15
   :end-line: 22

If you want to contribute, please make sure to keep the unit tests green and to deliver new ones, if you extend the functionality.
