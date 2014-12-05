debops.golang
#############


Install Go language (golang) support using Debian packages. You can choose
to install the system's default version of Go or use the 1.3.x version that
has been backported from Debian Jessie.

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.1``. To install it, run::

    ansible-galaxy install debops.golang


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.backporter``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Install either the 'apt' or 'backport' version of Golang
    #   'apt'      whatever version is available through apt on your OS/distro
    #   'backport' for when you're building the backport on your build server
    #
    # Versions for a few popular distros:
    #   Debian Wheezy: 1.0.2 -> backport version is 1.3.1
    #   Debian Jessie: 1.3.1
    #   Ubuntu Trusty: 1.2.1
    golang_version: 'apt'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.golang`` role was written by:

- Nick Janetakis | `e-mail <mailto:nick.janetakis@gmail.com>`__ | `Twitter <https://twitter.com/nickjanetakis>`__ | `GitHub <https://github.com/nickjj>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

