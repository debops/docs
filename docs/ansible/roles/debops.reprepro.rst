debops.reprepro
###############



``debops.reprepro`` role is used to create and manage local APT repository.
Packages can be uploaded manually to a specific user account, or they can
be downloaded by the role from specific directory on Ansible Controller.
Role will also automatically configure access to created APT repository on
all hosts managed by Ansible.

This role is by default not used directly by the playbook. Instead,
``debops.apt`` role uses it as a dependency.

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.reprepro


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.secret``
- ``debops.auth``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # The FQDN of the host on which reprepro is configured; other hosts in the
    # group/cluster will use this for obtaining apt keys and repository
    # information. Set to False to disable reprepro. By default, it is defined by the
    # 'apt' role in roles/apt/meta/main.yml
    reprepro: False
    
    # 'reprepro' role requires a webserver to serve repository data, but currently
    # it's not dependent on one, relying on 'apt' role to configure it beforehand.
    # This variable set by the 'apt' role specifies that 'reprepro' role can
    # configure it's APT repository (webserver is configured)
    reprepro_served: False
    
    # User and group for reprepro repository
    reprepro_user: 'reprepro'
    reprepro_group: 'reprepro'
    
    # User account of reprepro incoming queue (will be configured as sftponly account)
    reprepro_incoming_user: 'reprepro-upload'
    
    # Directory where reprepro will create the Debian repositories
    # By default it's the nginx document root directory for default server
    reprepro_repository: '/srv/www/sites/default/public/debian'
    
    # Install and then uninstall haveged during GPG key generation to make it faster
    # Useful during testing or on virtual machines, but may create weaker GPG keys
    # More information: https://security.stackexchange.com/questions/34523/
    reprepro_haveged: False
    
    # Settings for GPG key used to sign reprepro repository
    reprepro_gpg_key_type: 'RSA'
    reprepro_gpg_key_length: '2048'
    reprepro_gpg_name: 'Reprepro Automatic Signing Key'
    reprepro_gpg_email: 'root@{{ ansible_domain }}'
    reprepro_gpg_expire_days: '1825'
    
    # List of repositories managed by reprepro (for possible values see
    # man reprepro, section about 'conf/distributions' configuration file)
    reprepro_distributions:
    
      - codename: 'wheezy'
        components: 'main'
        suite: 'stable'
        architectures: 'amd64 i386'
        origin: 'Automatic Reprepro Repository'
        description: 'Automatic Reprepro Repository'
        label: 'reprepro-auto'
        signwith: 'yes'
    
      - codename: 'wheezy-backports'
        components: 'main'
        suite: 'stable-backports'
        architectures: 'amd64 i386'
        origin: 'Automatic Reprepro Backports Repository'
        description: 'Automatic Reprepro Backports Repository'
        label: 'reprepro-auto'
        signwith: 'yes'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.reprepro`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

