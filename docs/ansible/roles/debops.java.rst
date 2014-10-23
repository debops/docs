debops.java
###########

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-java.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-java

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--java-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-java/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.java-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1571



This role installs OpenJDK Java packages. It is useful as a dependency of
other roles.

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

- Nick Janetakis | `e-mail <mailto:nick.janetakis@gmail.com>`_ | `Twitter <https://twitter.com/nickjanetakis>`_ | `GitHub <https://github.com/nickjj>`_

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

