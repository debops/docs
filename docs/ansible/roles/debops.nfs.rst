debops.nfs
##########

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-nfs.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-nfs

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--nfs-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-nfs/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.nfs-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1579



This role can be used to configure NFSv3 client and server services between
many hosts in a group.

This role is an obsolete state and will be replaced in the future. Do not
use this role in a production environment.

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.nfs


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.ferm``
- ``debops.etc_services``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Enable to configure host as NFS server
    nfs_server: False
    
    # Define on NFS clients which server to use
    #nfs_host: 'nfs.{{ ansible_domain }}'
    
    # List of simple NFS shares, they will be created automatically
    # on NFS server: /srv/nfs/{{ item }}/
    # on NFS client: /media/nfs/{{ item }}/
    #nfs_simple:
    #  - 'home'
    #  - 'usr'
    
    # Options for simple NFS shares
    nfs_simple_exports: '/srv/nfs'
    nfs_simple_mounts: '/media/nfs'
    nfs_simple_hostname: '192.168.0.0/16'
    nfs_simple_options: 'rw,sync,subtree_check,root_squash'
    
    # Allow these networks and hosts to connect to NFS server
    nfs_server_allow:
      - '10.0.0.0/8'
      - '172.16.0.0/12'
      - '192.168.0.0/16'
    
    # List of custom NFS exports
    #nfs_server_exports:
    #  - '/home  192.168.0.0/16(rw,sync,subtree_check,root_squash)'
    #  - '/usr   192.168.0.0/16(rw,sync,subtree_check,root_squash)'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.nfs`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`_ | `Twitter <https://twitter.com/drybjed>`_ | `GitHub <https://github.com/drybjed>`_

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

