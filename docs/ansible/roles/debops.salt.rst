debops.salt
###########


This role will install and configure `SaltStack`_ master service, which can
be used to manage Salt minions. By default, Salt master packages from
upstream repositories will be installed and configured to listen on both
IPv4 and IPv6 networks and will accept connections from all hosts; you can
limit connections through the firewall using `debops.ferm`_ role.

.. _SaltStack: http://www.saltstack.com/
.. _debops.ferm: https://github.com/debops/ansible-ferm/

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.ferm``
- ``debops.etc_services``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # List of packages to install on Salt master host
    salt_packages: [ 'salt-master' ]
    
    # Lists of IP addresses or network CIDR ranges allowed to connect to Salt
    # master through the firewall. If lists are empty, anyone can connect.
    salt_allow: []
    salt_group_allow: []
    salt_host_allow: []
    
    # Configure Salt master using Ansible?
    salt_configuration: True
    
    # File with Ansible-generated Salt master configuration. If configuration is
    # disabled, it will be automatically removed by Ansible on the next run.
    salt_configuration_file: '/etc/salt/master.d/ansible.conf'
    
    # By default Salt master listens for connections on all IPv6 and IPv4
    # interfaces. If you want to disable IPv6, change the value to "0.0.0.0"
    salt_interface: '::'
    
    # Enable/Disable IPv6 support in Salt master
    salt_ipv6: True
    
    # Ports configured in firewall for Salt master
    salt_publish_port: '4505'
    salt_return_port: '4506'
    
    # Salt master worker multiplier
    salt_worker_multiplier: 2
    
    # Number of Salt master workers to run
    salt_worker_threads: '{{ (ansible_processor_cores | int * salt_worker_multiplier | int) }}'
    
    # Additional Salt master options in YAML text block format
    salt_options: False




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.salt`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

