Created by `Stephen McDonald <http://twitter.com/stephen_mcd>`_

Introduction
============

Do you have smaller Python projects that only need a README file
for documentation? Want to host your README on `Read The Docs`_?

sphinx-me is a `BSD licensed`_ tool that will create a `Sphinx`_
documentation shell for your project and include the README file
as the documentation index. It handles extracting the required meta
data such as the project name, author and version from your project
for use in your Sphinx docs.

Once you use sphinx-me to build your Sphinx docs, you can then
add your project to the Read The Docs site and have your project's
README hosted with an attractive Sphinx documentation theme.

.. note::

    Your README file should be in a `reStructuredText`_ compatible
    format.

Installation
============

The easiest way to install sphinx-me is directly from `PyPI`_ using
`pip`_ or `setuptools`_ by running the respective command below::

    $ pip install -U sphinx-me

or::

    $ easy_install -U sphinx-me

Otherwise you can download sphinx-me and install it directly
from source::

    $ python setup.py install

Running
=======

sphinx-me will be installed as a system-wide script that can be run from
the command line while in your project's root directory::

    $ sphinx-me

When run in your project's directory, it will create a ``docs`` directory
with two files, the Sphinx ``conf.py`` module, and an ``index.rst`` file
which will include your project's README.

The ``conf.py`` module calls a setup function from sphinx-me that sets up
the minimum required settings for your Sphinx docs.

  * ``project`` - the directory name of your project is used.
  * ``version`` - retrieved from the ``version`` arg of your
    ``setup.py`` script, or your package's ``__version__`` attribute.
  * ``copyright`` - retrieved from the ``author`` arg of your
    ``setup.py`` script, or your package's ``__author__`` attribute.

Running this process will also perform an initial ``sphinx-build``
inside your project's ``docs/build`` directory. Subsequent builds
after making changes to your README can be performed by running
sphinx-me again, or by using the regular ``sphinx-build`` command.

Hosting on Read The Docs
========================

When hosting your sphinx-me generated docs on `Read The Docs`_, you
must ensure you check the **Use virtualenv** option and specify
``sphinx-me`` as a requirement in either your ``setup.py`` script,
or in a `pip requirements file`_ that you'll need to also specify in
the **Requirements file** field for your project on Read The Docs.

.. _`Read The Docs`: http://readthedocs.org/
.. _`BSD licensed`: http://www.linfo.org/bsdlicense.html
.. _`Sphinx`: http://sphinx.pocoo.org/
.. _`reStructuredText`: http://docutils.sourceforge.net/rst.html
.. _`PyPI`: http://pypi.python.org/
.. _`setuptools`: http://pypi.python.org/pypi/setuptools
.. _`pip`: http://www.pip-installer.org/
.. _`pip requirements file`: http://www.pip-installer.org/en/latest/requirement-format.html
