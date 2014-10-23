debops.ansible
##############

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-role-ansible.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-role-ansible

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--role--ansible-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-role-ansible/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.ansible-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1550



``debops.ansible`` is an Ansible role which builds and installs Debian
package with specified Ansible version (by default, ``devel``). It can be
used to easily create remote Ansible Controller host or test your playbooks
on a ``devel`` Ansible version in a container or VM.

If ``redis-server`` is found on managed host, this role will automatically
enable support for host fact caching in Ansible.

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.ansible




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # ---- Ansible .deb package build ----
    
    # Ansible version to build
    role_ansible_version: 'devel'
    
    # User which will be used to clone and build Ansible
    # By default, current system user
    role_ansible_build_user: '{{ ansible_ssh_user | default(lookup("env","USER")) }}'
    
    # Where Ansible will be cloned and built, relative to user's $HOME
    role_ansible_build_path: 'src/github.com/ansible/ansible'
    
    # Ansible repository which will be cloned
    role_ansible_git_repository: 'https://github.com/ansible/ansible.git'
    
    
    # ---- /etc/ansible/ansible.cfg ----
    
    # Ansible will use 'inventory/' directory in local directory by default
    role_ansible_config_hostfile: 'inventory/'
    
    # How many forks to use by default
    role_ansible_config_forks: '5'
    
    # How Ansible should gather host facts during playbook execution
    role_ansible_config_gathering: 'smart'
    
    # List of directories to look for Ansible roles
    role_ansible_config_roles_path: [ '/etc/ansible/roles' ]
    
    # Should Ansible check SSH host fingerprint?
    role_ansible_config_host_key_checking: True
    
    # Default module to use if none is specified
    role_ansible_config_default_module_name: 'command'
    
    # Default hash behaviour, 'replace' or 'merge'
    role_ansible_config_hash_behaviour: 'replace'
    
    # Should Ansible display skipped hosts?
    role_ansible_config_display_skipped_hosts: True
    
    # Specify what fact caching mode to use, currently 'memory' or 'redis'. Leave
    # undefined to let Ansible role detect redis by itself
    role_ansible_config_fact_caching: ''
    
    # Timeout for cached host facts, by default 24h
    role_ansible_config_fact_caching_timeout: '{{ (60 * 60 * 24) }}'

List of internal variables used by the role::

    role_ansible_package_version
    role_ansible_fact_caching


Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.ansible`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

