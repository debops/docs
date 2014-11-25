debops.hwraid
#############

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-hwraid.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-hwraid

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--hwraid-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-hwraid/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.hwraid-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/2259



`HWRaid`_ is a repository of software packages useful on hosts with
hardware RAID storage arrays for Debian and Ubuntu Linux operating systems.

This role will configure the APT repository for supported distributions and
after checking list of loaded kernel modules, install recognized packages.
HWRaid packages contain a monitoring script, which will periodically send
a mail message to ``root`` account in case of issues with the RAID array.

Some of the software packages offered in HWRaid repository are not Open
Source, however there are no alternatives available.

.. _HWRaid: http://hwraid.le-vert.net/

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.hwraid




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # OS distribution used to lookup available releases
    hwraid_distribution: '{{ ansible_distribution }}'
    
    # OS release used to lookup available releases
    hwraid_release: '{{ ansible_distribution_release }}'

List of internal variables used by the role::

    hwraid_register_release


Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.hwraid`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

