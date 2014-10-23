debops.encfs
############

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-encfs.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-encfs

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--encfs-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-encfs/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.encfs-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1562



Ansible role ``debops.encfs`` allows you to create and manage directories
using `EncFS`_, FUSE-based encrypted virtual filesystem.

.. _EncFS: https://en.wikipedia.org/wiki/EncFS

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.4``. To install it, run::

    ansible-galaxy install debops.encfs




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Absolute path to a directory where encrypted filesystem will be mounted
    # Required
    encfs: False
    
    # Suffix of the directory with encrypted filesystem, it will be created in the
    # same path as the mount directory
    encfs_suffix: ".encrypted"
    
    # List of GPG keys to use to encrypt encfs keyfile. GPG encryption is supported
    # only on localhost (hosts which have ansible_connection=local set). Without
    # list of GPG recipients, GnuPG will ask for a passphrase instead
    encfs_gpg: []
    
    # Password to use instead of GPG keys / GPG passphrase. Supports encfs on
    # remote hosts. Will be sent via stdout and visible in 'ps' and Ansible logs,
    # use an external file with encfs_passfile to mitigate that.
    # You can populate this variable from an external file using lookup('file','path')
    encfs_password: False
    
    # An absolute path to file on remote host to store the password in transit.
    # Will be shredded when no longer needed. encfs role creates two files with this
    # name + suffixes '_init' and '_pass'
    encfs_passfile: False
    
    # By default encfs role behaves as a toggle - opens the encrypted filesystem if
    # it's closed, closes it if opened. By setting encfs_mode (for example with
    # --extra-vars) you can force desired mode of operation:
    #  - 'open' - create or open encrypted filesystem
    #  - 'close' - close encrypted filesystem
    encfs_mode: False
    
    # Device to use as source of randomness. You can change that to '/dev/urandom'
    # to use faster but weaker randomness source
    encfs_random: '/dev/random'

List of internal variables used by the role::

    encfs_user


Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.encfs`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

