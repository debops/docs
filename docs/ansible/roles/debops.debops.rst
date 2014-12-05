debops.debops
#############


Install DebOps scripts, and optionally automatically download DebOps
playbooks and roles and install them system-wide in `/usr/local`. This role
can be used to easily setup a remote Ansible Controller using Ansible.

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.debops




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # List of packages required by DebOps, if you don't want to install Ansible
    # from a Debian package, you can remove it here
    debops_packages: [ 'ansible', 'python-netaddr' ]
    
    # URL to main DebOps repository
    debops_source_url: 'https://github.com/debops/debops'
    
    # Path where DebOps source repository will be cloned
    debops_source_path: '/usr/local/src/github.com/debops/debops'
    
    # git branch name to clone and update
    debops_source_version: 'master'
    
    # Should DebOps playbooks and roles be installed automatically system-wide?
    # This will be an async operation and it can take a while to complete
    debops_playbooks_systemwide: False




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.debops`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

