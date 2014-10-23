debops.tcpwrappers
##################

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-tcpwrappers.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-tcpwrappers

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--tcpwrappers-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-tcpwrappers/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.tcpwrappers-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1604



This role can be used to manage `TCP Wrappers`_ rules located in
``/etc/hosts.allow`` (by default all hosts will be denied access in
``/etc/hosts.deny``, but this can be disabled by a variable).

Other roles can use this role as a dependency to manage access to their own
services (for example, ``debops.mysql``, ``debops.sshd``).

By default, tcpwrappers will be configured to block access from everywhere
except ``localhost`` (relative to remote host) and Ansible Controller.

.. _TCP Wrappers: https://en.wikipedia.org/wiki/TCP\_Wrapper

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.tcpwrappers




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Should Ansible manage tcpwrappers configuration?
    tcpwrappers: True
    
    # Optional list of CIDR hosts which will be allowed to connect to sshd service.
    # Entries are saved in the local facts on remote hosts.
    # Remember to specify IP address from the remote host point of view.
    # Format: "IP address/netmask", for example: '192.168.1.1/32'
    tcpwrappers_ansible_controllers: []
    
    # Deny access from all hosts/networks by default?
    tcpwrappers_deny_all: True
    
    # Lists of /etc/hosts.allow entries. Example entry below
    tcpwrappers_allow: []
    tcpwrappers_group_allow: []
    tcpwrappers_host_allow: []
    
      #- daemon: 'ALL'            # daemon to configure (sshd, mysqld, etc.)
      #  client: []               # list of host or network addresses.
                                  # If empty, entry will be removed
      #  weight: '10'             # filename prefix, helps with sorting, optional
      #  filename: ''             # custom filename, optional
      #  comment: ''              # comment, optional
    
      #- custom: |                  # custom, free-form text block (filename required)
      #    # Custom entry
      #    # Text block
      #  filename: 'custom_entry'
    
    # Access from localhost
    tcpwrappers_local_allow:
      - daemon: 'ALL'
        client: [ '127.0.0.0/8', '[::1]/128' ]
        comment: 'Access from localhost'
        filename: 'allow_localhost'
        weight: '06'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.tcpwrappers`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

