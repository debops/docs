debops.debug
############

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-debug.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-debug

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--debug-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-debug/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.debug-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1558



Dump all variables used by Ansible during playbook run to a file for
inspection. This role is not active during normal playbook operation and
should be used for development only.

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.debug




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Where to save all Ansible variables
    debug_variables: '/tmp/ansible_variables'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.debug`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`_ | `Twitter <https://twitter.com/drybjed>`_ | `GitHub <https://github.com/drybjed>`_

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

