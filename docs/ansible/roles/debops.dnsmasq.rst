debops.dnsmasq
##############

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-dnsmasq.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-dnsmasq

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--dnsmasq-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-dnsmasq/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.dnsmasq-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1561



This role installs and configures ``dnsmasq`` as a local DNS, DHCP and
PXE/TFTP server. At the moment configuration is limited, and resulting
environment is suited for local development only. A NATted network can also
be configured for ease of use for local virtual machines / LXC containers
without the need for additional external IP addresses.

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.dnsmasq


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.ferm``
- ``debops.tcpwrappers``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # 192.168.x.0/24 subnet to use in dnsmasq configuration
    dnsmasq_subnet: 32
    
    # Should dnsmasq support PXE Boot / TFTP server?
    dnsmasq_netboot: True
    
    # List of hosts/networks allowed to connect to TFTP server
    dnsmasq_netboot_allow: []
      #'192.168.32.0/24'
    
    # Network interface dnsmasq should listen on (configured for NAT by default)
    dnsmasq_interface: 'br2'
    
    # Local domain configuration for NAT
    dnsmasq_subdomain: 'nat'
    dnsmasq_domain: '{{ dnsmasq_subdomain }}.{{ ansible_fqdn }}'
    
    # Hostname of router/gateway interface
    dnsmasq_domain_gw: 'gw'
    
    # Hostname of local domain mail server
    dnsmasq_domain_mx: 'gw'
    
    # List of domain->IP address mappings returned by dnsmasq
    dnsmasq_address: {}
      #'subdomain.example.org': '10.20.30.40'
      #'.wildcard.example.org': '10.50.60.70'
    
    # List of CNAME entries
    dnsmasq_cname: {}
      #'host.example.net': 'other.example.net'
      #'sub.domain.example.org': 'other.example.net'
    
    # List of CNAME entries on local domain
    dnsmasq_cname_subdomain: {}
      #'host': 'other'
      #'sub.domain': 'other'
    
    # Enable or disable DHCP service
    dnsmasq_dhcp: True
    
    # DHCP range (2-254)
    dnsmasq_dhcp_range: '192.168.{{ dnsmasq_subnet }}.2,192.168.{{ dnsmasq_subnet }}.254'
    
    # Default DHCP lease time
    dnsmasq_lease_time: '24h'
    
    # Default router/gateway address
    dnsmasq_router: '192.168.{{ dnsmasq_subnet }}.1'
    
    # Reverse DNS domain mapping
    dnsmasq_revdns: '{{ dnsmasq_subnet }}.168.192.in-addr.arpa'
    
    # NAT network to configure
    dnsmasq_network: '192.168.{{ dnsmasq_subnet }}.0/24'
    
    # Tag used in dnsmasq configuration options
    dnsmasq_tag: 'debops{{ dnsmasq_interface }}'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.dnsmasq`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`_ | `Twitter <https://twitter.com/drybjed>`_ | `GitHub <https://github.com/drybjed>`_

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

