debops.pki
##########

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-pki.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-pki

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--pki-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-pki/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.pki-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1588



This role is meant to be a simple SSL certificate manager which:

* creates self-signed certificate for a host, along with a CSR;

* uploads the CSR for its certificate to Ansible Controller for easy
  signing by a CA;

* downloads signed certificate from Ansible Controller when it becomes
  available;

* downloads custom CA or wildcard certificates provided to the role by
  administrator in a specifc directory on Ansible Controller;

``debops.pki`` role is planned to be rewritten to support automatic CA
signing and custom certificates for clients/applications.

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.pki


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.secret``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Should PKI be managed by Ansible
    pki: True
    
    # Copy wildcard certificates and keys to remote hosts?
    pki_wildcard: True
    
    pki_path: '/srv/pki'
    pki_private_group: 'ssl-cert'
    
    pki_digest: 'sha256'
    pki_bits: 2048
    pki_selfsign_days: 365
    
    # Default settings for new Certificate Requests
    pki_country:            'AA'
    pki_state:              '{{ ansible_domain | capitalize }} State'
    pki_locality:           '{{ ansible_domain | capitalize }} City'
    pki_organization:       '{{ ansible_domain | capitalize }} Organization'
    pki_organizationalUnit: '{{ ansible_domain | capitalize }} Department'
    pki_commonName:         '{{ ansible_fqdn }}'
    pki_email:              'root@{{ ansible_domain }}'
    
    # Default certificate for FQDN of a host
    pki_default_certificate:
      - cn: '{{ ansible_fqdn }}'
    
    # Example list of host certificates to create
    #pki_host_certificates:
    #  - cn: 'example.com'
    #    mail:
    #      - 'root@example.com'
    #    dns:
    #      - 'www.example.com'
    #      - 'mail.example.com'
    #      - '*.mail.example.com'
    #    uri:
    #      - 'http://example.com/'
    #    ip:
    #      - '192.0.2.1'
    #
    #  - cn: 'subdomain.{{ ansible_domain }}'
    #
    #  - cn: 'other.{{ ansible_domain }}'
    #    ou: 'Other Department'
    #    e: 'root@other.{{ ansible_domain }}'
    #    mail:
    #      - 'others@other.{{ ansible_domain }}'
    #      - 'root@{{ ansible_domain }}'
    #    dns:
    #      - '*.other.{{ ansible_domain }}'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.pki`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

