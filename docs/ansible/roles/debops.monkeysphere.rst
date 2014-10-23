debops.monkeysphere
###################

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-monkeysphere.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-monkeysphere

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--monkeysphere-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-monkeysphere/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.monkeysphere-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1576



This role can be used to give SSH users the ability to login to the server
using their PGP/GnuPG keys. This functionality is enabled using
`Monkeysphere`_ project.

At the moment role is not fully complete. Required user configuration
functionality is in the works.

.. _Monkeysphere: http://web.monkeysphere.info/

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.monkeysphere




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Should monkeysphere be enabled? Disabled by default due to required manual
    # preparations, see: http://web.monkeysphere.info/getting-started-admin/
    monkeysphere: False
    
    # Should monkeysphere automatically publish new keys to Web of Trust?
    monkeysphere_autopublish: False
    
    # List of identity certifiers to add automatically at first setup (omit 0x)
    monkeysphere_default_identity_certifiers: False
    
    # At what minute each hour monkeysphere should update the user authorized_keys?
    monkeysphere_update_minute: '42'
    
    # Keyserver to use (default frontend from 'sks' role). You might want to setup
    # an internal-only frontend or backend to mitigate availability problems
    monkeysphere_keyserver: 'keyserver.{{ ansible_domain }}'
    
    # Default keyserver from monkeysphere configuration, public GPG Web of Trust
    #monkeysphere_keyserver: 'pool.sks-keyservers.net'
    
    # Should monkeysphere check the keyserver on each connection?
    monkeysphere_check_keyserver: 'false'
    
    # Log verbosity (SILENT, ERROR, INFO, VERBOSE, DEBUG)
    monkeysphere_log_level: 'INFO'
    
    # System user that controls the monkeysphere GPG keyring
    monkeysphere_user: 'monkeysphere'
    
    # Look for user ids in system-wide directory
    monkeysphere_authorized_user_ids: '/etc/monkeysphere/authorized_user_ids/%u'
    
    # Don't combine user's authorized_keys, sshd supports multiple files
    monkeysphere_raw_authorized_keys: 'none'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.monkeysphere`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

