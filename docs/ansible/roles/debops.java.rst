debops.java
###########



This role installs OpenJDK Java packages. It is useful as a dependency of
other roles.

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.java




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Available options for installing Java Open JDK:
    #   7-jre
    #   6-jre
    #   7-jdk
    #   6-jdk
    java_versions:
      - '7-jre'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.java`` role was written by:

- Nick Janetakis | `e-mail <mailto:nick.janetakis@gmail.com>`__ | `Twitter <https://twitter.com/nickjanetakis>`__ | `GitHub <https://github.com/nickjj>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

