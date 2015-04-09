debops.radvd
############



``debops.radvd`` role manages `Router Advertisement Daemon`_.
``radvd`` periodically sends router advertisements and other hosts on the
network will automatically pick them up. This results in them obtaining an
IPv6 address and internet connectivity.

.. _Router Advertisement Daemon: https://en.wikipedia.org/wiki/Radvd

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.radvd




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---

    # ---- Default options ----

    # Network interface to configure
    # By default, configure on interface created by 'debops.subnetwork' role
    radvd_default_interface: 'br2'

    # Options for default interface, specified as YAML text block
    radvd_default_interface_options: |
      AdvSendAdvert on;
      MaxRtrAdvInterval {{ radvd_max_advert_interval }};
      {% if radvd_default_dhcpv6 is defined and radvd_default_dhcpv6 %}
      AdvManagedFlag on;
      AdvOtherConfigFlag on;
      {% endif %}

    # Options defined for default prefixes as YAML text block
    radvd_default_prefix_options: ''

    # Enable or disable support for DHCPv6 server in default configuration
    radvd_default_dhcpv6: True


    # ---- DNS and search domains ----

    # Local subdomain leaf to advertise in DNSSL
    radvd_default_subdomain: 'lan'

    # List of search domains to advertise in DNSSL
    radvd_default_domains: [ '{{ radvd_default_subdomain }}.{{ ansible_fqdn }}', '{{ ansible_domain }}' ]


    # ---- radvd configuration ----

    # Maximum time between router advertisements, in seconds
    radvd_max_advert_interval: '60'

    # See radvd.conf(5) for documentation of available options. Each section is
    # specified with lowercase name, section options are specified as YAML text
    # blocks (semicolons at the end of each line are required).
    radvd_interfaces:

        # Default interface created by 'debops.subnetwork' role
      - interface: '{{ radvd_default_interface }}'
        comment: 'Default configuration for local network'

        # Interface options as YAML text block
        options: '{{ radvd_default_interface_options }}'

        # List of prefixes advertised on this interface
        prefixes:
          - prefix: '::/64'
            options: '{{ radvd_default_prefix_options }}'

        # List of configured routes for this interface
        routes: []
          #- route: ''
          #  options: |

        # List of nameservers advertised on this interface
        nameservers: []
          #- rdnss: []
          #  options: |

        # List of search domains advertised on this interface
        domains:
          - dnssl: '{{ radvd_default_domains }}'

        # List of clients to advertise to, if not defined, advertise to all hosts
        # on this interface
        clients: []




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.radvd`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

