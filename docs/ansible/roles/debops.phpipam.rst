debops.phpipam
##############



This role installs `phpIPAM`_, an IP Address Manager written in PHP5. MySQL
will be used as the backend database, and nginx will be a frontend
webserver.

Currently phpIPAM is deployed from DebOps repository on Github, that might be
changed in the future.

Default credentials: ``Admin:ipamadmin``

.. _phpIPAM: http://phpipam.net/

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.phpipam


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.secret``
- ``debops.nginx``
- ``debops.php5``
- ``debops.mysql``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Should phpipam role manage it's own dependencies?
    phpipam_dependencies: True
    
    # Domain on which phpIPAM is configured in nginx
    phpipam_domain: [ 'ipam.{{ ansible_domain }}' ]
    
    # phpIPAM source repository and version to deploy
    phpipam_source_address: 'https://github.com/ginas/'
    phpipam_source_repository: 'phpipam.git'
    phpipam_source_version: 'master'
    
    # phpIPAM database configuration
    phpipam_database_host: 'localhost'
    phpipam_database_user: 'phpipam'
    phpipam_database_name: 'phpipam'
    
    # List of hosts or networks in CIDR format allowed to access phpIPAM
    # If empty, allws access from all networks
    phpipam_allow: []

List of internal variables used by the role::

    phpipam_database_password


Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.phpipam`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

