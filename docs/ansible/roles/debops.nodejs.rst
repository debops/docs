debops.nodejs
#############



This role can be used as a dependency for other roles to provide NodeJS and
npm support.

At the moment, on Debian Wheezy a ``nodejs`` package from
``wheezy-backports`` is installed, and `npm` command is installed from
upstream using a script; this will be changed in the future to install
``npm`` package as a backported Debian Jessie version.

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.nodejs




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # List of packags to install
    nodejs_packages: [ 'nodejs', 'nodejs-legacy' ]




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.nodejs`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

