debops.directories
##################

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-directories.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-directories

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--directories-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-directories/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.directories-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1560



This is a simple wrapper role around ``file`` Ansible module, which lets
you manage (create, modify or remove) directories using inventory
variables, including creation on multiple hosts at once.

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.directories




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # List of global directories
    directories_list: []
    
      #- path: '/tmp/directory'             # required
      #  state: 'directory'
      #  owner: 'root'
      #  group: 'root'
      #  mode: '0755'
    
    # List of directories in a host group
    directories_group_list: []
    
    # List of directories on a specific host
    directories_host_list: []




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.directories`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`_ | `Twitter <https://twitter.com/drybjed>`_ | `GitHub <https://github.com/drybjed>`_

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

