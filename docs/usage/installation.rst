Installation
============

This Modul have Many Ways to Install

pip
---

That is the Easiest Way to Install pacflypy, we use the PyPa registry to install it.

Depends For this:

1. You need min. Python3.8 Installed
2. You need pip3 installed (For Ubuntu and Debian talk we later, the Best Installation Way)

.. code-block:: bash

    pip install --no-cache-dir -U pacflypy


git and setup.py
----------------

That is an Other Way and you don't need directly pip.

Depends For this:

1. You need min. Python3.8 Installed
2. You need setuptools installed, but Not pip
3. You need git installed

.. code-block:: bash

    git clone https://github.com/pacflypy/pacflypy.git
    cd pacflypy
    python3 setup.py --install

git and pip, local
------------------

That is a Way to Install the Modul via git and pip

Depends For this:

1. You need min. Python3.8 Installed
2. You need pip installed
3. You need git installed

.. code-block:: bash

    git clone https://github.com/pacflypy/pacflypy.git
    cd pacflypy
    pip install --no-cache-dir -U .

directly from git archive
-------------------------

The Best on this way ist, you become the Newest Version and you not need git for this

1. You need min. Python3.8 Installed
2. You need pip Installed

.. code-block:: bash

    pip install --no-cache-dir -U https://github.com/pacflypy/pacflypy/archive/master.zip

On Debian and Ubuntu
--------------------

Ubuntu and Debian allow not directly the Installation from Python Modules, system withe
For Ubuntu and Debian have i Under Releases a Debian Installation Package, you can Install Him Easy

.. code-block:: bash

    version='0.2.6'
    wget https://github.com/pacflypy/pacflypy/releases/download/v.${version}/python3-pacflypy_${version}_all_debian.deb
    if ! command -v sudo &> /dev/null; then
        dpkg -i python3-pacflypy_${version}_all_debian.deb
    else
        sudo dpkg -i python3-pacflypy_${version}_all_debian.deb
    fi
    rm -rf python3-pacflypy_${version}_all_debian.deb

