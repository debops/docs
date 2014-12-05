debops.sks
##########



`SKS Keyserver`_ is an OpenPGP/GnuPG key server. This role allows you to
install and manage one or more keyservers in a cluster. Specified host (by
default first host in ``[debops_sks]`` Ansible group) will also be
configured as a web frontend to the cluster (``nginx`` will be used as the
frontend webserver).

You can use ``debops.sks`` role to create your own keyserver pool (and in
extension your own OpenPGP Web of Trust) or `connect to an existing pool`_.
In the latter case, role supports an option to not initialize the database
by default, in which case you can seed your local key database from
a keyserver dump (which is a preferred option of connecting to the existing
pool because of the size of existing key database dumps).

.. _SKS Keyserver: http://sks-keyservers.net/
.. _connect to an existing pool: http://www.keysigning.org/sks/

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.sks


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.ferm``
- ``debops.etc_services``
- ``debops.apt_preferences``
- ``debops.nginx``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Automatically create keyserver database? Database will be empty
    # If you want to seed the database with public GPG keys or connect to public
    # SKS Keyserver network, you should set this variable to "False" and seed the
    # database manually. See: http://keysigning.org/sks/
    sks_autoinit: False
    
    # GPG fingerprint of server administrator
    sks_contact: ''
    
    # From header for outgoing mail
    sks_from: 'PGP Key Server <pgp-public-keys@{{ ansible_fqdn }}>'
    
    # DNS domain on which SKS frontend webserver should be configured
    sks_domain: [ 'keyserver.{{ ansible_domain }}' ]
    
    # Ansible group of hosts which are included in SKS cluster
    sks_cluster: '{{ groups.debops_sks }}'
    
    # List of inventory hosts which provide frontend web service
    sks_frontends: [ '{{ sks_cluster[0] }}' ]
    
    # List of hosts which can connect to hkp service. If this list is empty,
    # anybody can connect.
    sks_hkp_allow: []
    
    # List of public SKS keyservers you want to peer with. It's a list of simple
    # lines, which allows you to include custom ports and comments (see sks(8)
    # documentation). It's good etiquette to ask someone for permission before you
    # add their server to this list (and their server needs to have yours for the
    # communication to work).
    # You should probably connect only one of your private keyservers to the public
    # keyserver network, your other servers will propagate the changes between
    # themselves.
    sks_public_list: []
    #  - name: 'keyserver.example.org'
    #    port: '{{ sks_recon_port }}'
    #    email: 'Server Administrator <root@example.org'
    #    gpg: '0xDEADBEEF'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.sks`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

