debops.nat
##########

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-nat.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-nat

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--nat-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-nat/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.nat-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1578



``debops.nat`` is a helper role which configures internal network on
a separate bridge interface with NAT or MASQUERADE firewall configuration
(network will use non-routable IP address space and access to the Internet
will be provided by the host operating system). This network can be used as
a development environment for virtual machines or containers.

Configuration of iptables firewall / forwarding and network interfaces will
be performed by ``debops.ferm`` and ``debops.ifupdown`` Ansible roles.

You can use ``dnsmasq`` server (available via ``debops.dnsmasq`` Ansible
role) to complete the network configuration and provide internal DNS/DHCP
server.

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.nat


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.ferm``
- ``debops.ifupdown``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # 192.168.x.0/24 subnet to use by default for NAT
    nat_subnet: 32
    
    # Network interface to use for NAT bridge
    nat_interface: 'br2'
    
    # Network configuration
    nat_address: '192.168.{{ nat_subnet }}.1'
    nat_netmask: '255.255.255.0'
    nat_network: '192.168.{{ nat_subnet }}.0'
    nat_broadcast: '192.168.{{ nat_subnet }}.255'
    
    # Should iptables use masquerading?
    # True - static IP route to outside network
    # False - dynamic masquerading
    nat_masquerade: False
    
    # Default NAT domain
    nat_subdomain: 'nat'
    nat_domain: '{{ nat_subdomain }}.{{ ansible_fqdn }}'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.nat`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

