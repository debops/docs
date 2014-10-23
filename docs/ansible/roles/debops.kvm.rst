debops.kvm
##########

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-kvm.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-kvm

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--kvm-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-kvm/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.kvm-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1572



This role installs packages required for KVM support on a host. You can
then access this host with, for example, ``virt-manager`` to create and
manage KVM virtual machines.

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.kvm




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # List of administrator accounts which should have access to libvirtd
    kvm_admins: [ '{{ ansible_ssh_user }}' ]
    
    # UNIX group that has access to libvirtd
    kvm_group: 'libvirt'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.kvm`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

