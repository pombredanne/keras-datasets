keras\_datasets
===============

A repository hosting keras dataset generators

|Open Source Love| |license| |GitHub release| |Build Status| |Coverage
Status| |PyPI| |PyUP Updates| |Python 3| |Documentation Status|

Issues
======

Feel free to submit issues and enhancement requests.

Copyright and Licensing
=======================

The project is released under the GNU General Public License v3.0, which
gives you the following rights in summary:

+--------------------+-------------------+----------------------------------+
| **Permissions**    | **Limitations**   | **Conditions**                   |
+====================+===================+==================================+
| *Commercial use*   | *Liability*       | *License and copyright notice*   |
+--------------------+-------------------+----------------------------------+
| *Modification*     | *Warranty*        |                                  |
+--------------------+-------------------+----------------------------------+
| *Distribution*     |                   |                                  |
+--------------------+-------------------+----------------------------------+
| *Private use*      |                   |                                  |
+--------------------+-------------------+----------------------------------+

Contributing guidelines
=======================

Please have a look to the `Contributing Guidelines <CONTRIBUTING.md>`__
first.

We follow the "fork-and-pull" Git workflow.

1. **Fork** the repo on GitHub
2. **Clone** the project to your own machine
3. **Commit** changes to your own branch
4. **Push** your work back up to your fork
5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull
request!

Installation
------------

Available with the Python Package Index:
https://github.com/DEKHTIARJonathan/keras-datasets/

.. code:: shell

    pip install keras-datasets

.. code:: shell

    ## First clone the repository
    git clone https://github.com/DEKHTIARJonathan/keras-datasets.git

    ## Create a virtualenv
    virtualenv venv

    # Linux: activate the virtualenv
    source venv/bin/activate

    # Windows activate the virtualenv
    venv\Scripts\activate.bat

    ## Then install the library
    pip install -r requirements.txt

    ## Then install the library
    python setup.py install

3. Running Unit Tests
=====================

.. code:: sh

    # Linux
    source venv/bin/activate

    # Windows
    venv\Scripts\activate.bat

    # Then
    coverage run manage.py test
    coverage report -m
    coverage html

.. |Open Source Love| image:: https://badges.frapsoft.com/os/v2/open-source.svg?v=103
   :target: https://opensource.org/licenses/MIT/
.. |license| image:: https://img.shields.io/github/license/DEKHTIARJonathan/keras-datasets.svg
   :target: https://github.com/DEKHTIARJonathan/keras-datasets/releases
.. |GitHub release| image:: https://img.shields.io/github/release/DEKHTIARJonathan/keras-datasets.svg
   :target: https://github.com/DEKHTIARJonathan/keras-datasets
.. |Build Status| image:: https://travis-ci.org/DEKHTIARJonathan/keras-datasets.svg?branch=master
   :target: https://travis-ci.org/DEKHTIARJonathan/keras-datasets
.. |Coverage Status| image:: https://coveralls.io/repos/github/DEKHTIARJonathan/keras-datasets/badge.svg?branch=master
   :target: https://coveralls.io/github/DEKHTIARJonathan/keras-datasets?branch=master
.. |PyPI| image:: https://img.shields.io/pypi/v/keras-datasets.svg
   :target: https://pypi.python.org/pypi/keras-datasets/
.. |PyUP Updates| image:: https://pyup.io/repos/github/DEKHTIARJonathan/keras-datasets/shield.svg
   :target: https://pyup.io/repos/github/DEKHTIARJonathan/keras-datasets/
.. |Python 3| image:: https://pyup.io/repos/github/DEKHTIARJonathan/keras-datasets/python-3-shield.svg
   :target: https://pyup.io/repos/github/DEKHTIARJonathan/keras-datasets/
.. |Documentation Status| image:: https://readthedocs.org/projects/keras-datasets/badge/?version=latest
   :target: http://keras-datasets.readthedocs.io/en/latest/?badge=latest
