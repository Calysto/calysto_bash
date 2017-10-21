A Calysto Jupyter kernel for Bash.

To install::

    pip install calysto_bash

To use it, run one of:

.. code:: shell

    jupyter notebook
    # In the notebook interface, select 'Calysto Bash' from the 'New' menu
    ipython qtconsole --kernel calysto_bash
    ipython console --kernel calysto_bash

This is based on `MetaKernel <http://pypi.python.org/pypi/metakernel>`_,
which means it features a standard set of %%magics.

A sample notebook is available online_.


Advanced Installation Notes::
We automatically install a Jupyter kernelspec when installing the 
python package.  This location can be found using ``jupyter kernelspec list``.
If the default location is not desired, you can remove the directory for the
``calysto_bash`` kernel, and install using `python -m calysto_bash install`.  See
``python -m calysto_bash install --help`` for available options.


.. _online: http://nbviewer.ipython.org/github/Calysto/calysto_bash/blob/master/calysto_bash.ipynb
