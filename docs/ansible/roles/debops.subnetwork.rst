debops.subnetwork
#################

|Travis CI| |test-suite|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-subnetwork.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-subnetwork

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--subnetwork-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-subnetwork/



``debops.subnetwork`` is an Ansible role that creates and manages a local
network behind a bridge interface. It could also manage internal router
interfaces to a LAN. You can specify an IPv4 subnet and one or more
IPv6 subnets to configure it, the role will automatically configure basic
forwarding in any firewall and NAT for the IPv4 network.

This role requires ``ipaddr()`` filter plugin which is available in
`debops/debops-playbooks`_.

.. _debops/debops-playbooks: https://github.com/debops/debops-playbooks/

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.ferm``
- ``debops.ifupdown``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # ---- Network interfaces and firewall ----
    
    # Network interface to configure, by default a bridge
    subnetwork_iface: 'br2'
    
    # Network interfaces to attach to a bridge on ifup
    subnetwork_bridge_ports: [ 'none' ]
    
    # Enable packet forwarding from internal network to the outside world
    subnetwork_forwarding: True
    
    
    # ---- IPv4 network ----
    
    # IPv4 address set at the interface, in the 'host/prefix' format. It should be
    # an address of local network gateway, for example '192.0.2.1/24'. Only one
    # IPv4 address is supported
    subnetwork_ipv4: ''
    
    # Should IPv4 network be configured behind NAT? You might want to disable this
    # and configure routing elsewhere if you have public IPv4 subnet
    subnetwork_ipv4_nat: True
    
    # Should IPv4 traffic from internal network be masqueraded? If disabled, static
    # SNAT with default IPv4 address of the gateway will be configured instead.
    # Leave it True if you use a laptop or change networks frequently
    subnetwork_ipv4_nat_masquerade: True
    
    # Network interface to the default IPv4 gateway
    subnetwork_ipv4_gateway: '{{ ansible_default_ipv4.interface | default("") }}'
    
    # Additional options passed to the ifupdown configuration for IPv4 network,
    # in YAML text block format
    subnetwork_ipv4_options: ''
    
    
    # ---- IPv6 network ----
    
    # List of IPv6 addresses configured at the interface (multiple IPv6 addresses
    # are supported). You can configure here your own IPv6 prefixes from the
    # upstream router. If you don't have your own prefixes, you can set an ULA
    # prefix instead, for example from http://unique-local-ipv6.com/
    # CIDR /64 prefix is preferred for local network,
    # You need to specify addresses in 'host/prefix' format, with IPv6 address of
    # the gateway (ending with '::1'), for example: [ '2001:db8:2c33:deb0::1/64' ]
    subnetwork_ipv6: []
    
    # Network interface to the default IPv6 gateway
    subnetwork_ipv6_gateway: '{{ ansible_default_ipv6.interface | default("") }}'
    
    # Additional options passed to the ifupdown configuration for IPv6 network,
    # in YAML text block format
    subnetwork_ipv6_options: ''
    
    
    # ---- ifupdown interface templates ----
    
    # List of additional interfaces to configure before the main bridge
    subnetwork_ifupdown_prepend_interfaces: []
    
    # List of network interfaces to configure for the local network
    subnetwork_ifupdown_interfaces:
    
        # IPv4 network + bridge
      - iface: '{{ subnetwork_iface }}'
        type: '{% if subnetwork_iface | search("^br*") %}bridge{% else %}interface{% endif %}'
        inet: '{% if subnetwork_ipv4 | ipv4("host/prefix") %}static{% else %}manual{% endif %}'
        filename: 'subnetwork_{{ subnetwork_iface }}_ipv4'
        weight: '40'
        options: |
          {% if subnetwork_ipv4 | ipv4('host/prefix') %}
          address        {{ subnetwork_ipv4 | ipaddr('address') }}
          network        {{ subnetwork_ipv4 | ipaddr('network') }}
          netmask        {{ subnetwork_ipv4 | ipaddr('netmask') }}
          broadcast      {{ subnetwork_ipv4 | ipaddr('broadcast') }}
          {% endif %}
          {% if subnetwork_iface | search('^br.*') %}
          bridge_ports   {{ subnetwork_bridge_ports | join(' ') }}
          bridge_stp     on
          bridge_fd      0
          bridge_maxwait 0
          {% endif %}
          {% if subnetwork_ipv4_options %}
          {{ subnetwork_ipv4_options }}
          {% endif %}
    
        # IPv6 network
      - iface: '{{ subnetwork_iface }}'
        type: 'interface'
        inet6: '{% if subnetwork_ipv6 | unique | ipv6("host/prefix") %}static{% else %}manual{% endif %}'
        filename: 'subnetwork_{{ subnetwork_iface }}_ipv6'
        weight: '40'
        auto: False
        force: True
        options: |
          pre-up echo 0 > /proc/sys/net/ipv6/conf/{{ subnetwork_iface }}/accept_dad
          {% set subnetwork_var_ipv6_subnets = subnetwork_ipv6 | unique | ipv6('host/prefix') %}
          {% if subnetwork_var_ipv6_subnets %}
          address {{ subnetwork_var_ipv6_subnets[0] }}
          {% if subnetwork_var_ipv6_subnets | length > 1 %}
          {% for subnet in subnetwork_var_ipv6_subnets[1:] %}
          up   /sbin/ip address add {{ subnet }} dev {{ subnetwork_iface }}
          down /sbin/ip address del {{ subnet }} dev {{ subnetwork_iface }}
          {% endfor %}{% endif %}
          {% endif %}
          {% if subnetwork_ipv6_options %}
          {{ subnetwork_ipv6_options }}
          {% endif %}




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.subnetwork`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

