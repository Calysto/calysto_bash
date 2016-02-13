A Calysto Jupyter kernel for Bash.

To install::

    pip install bash_kernel
    python -m bash_kernel.install

To use it, run one of:

.. code:: shell

    jupyter notebook
    # In the notebook interface, select 'Calysto Bash' from the 'New' menu
    ipython qtconsole --kernel calysto_bash
    ipython console --kernel calysto_bash

This is based on `MetaKernel <http://pypi.python.org/pypi/metakernel>`_,
which means it features a standard set of %%magics.

A sample notebook is available online_.


.. _online: http://nbviewer.ipython.org/github/Calysto/bash_kernel/blob/master/bash_kernel.ipynb
