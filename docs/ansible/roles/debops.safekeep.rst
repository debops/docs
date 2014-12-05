debops.safekeep
###############



This role will configure `SafeKeep`_ scripts to create daily, incremental,
centralized backups on a specified server, based on ``rdiff-backup``.

Currently SafeKeep packages are not available in Debian repositories; you
need to provide the packages to APT using some other way, for example via
local APT repository created using ``debops.reprepro`` role.

.. _SafeKeep: http://safekeep.sourceforge.net/

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.safekeep


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.secret``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # FQDN hostname of SafeKeep server to which other clients will be backed up
    safekeep: ""
    
    # Should SafeKeep be enabled for current (client) host?
    safekeep_enabled: 'true'
    
    # Retention time for incremental backup
    safekeep_retention: '7D'
    
    # List of additional FQDN hosts to add to SafeKeep server ~/.ssh/known_hosts
    # You should configure here hosts that are outside of Ansible cluster (not
    # controlled by a playbook) that you want to backup using SafeKeep manually
    safekeep_keyscan: []
    
    # Shell script to execute on client host during various stages of backup
    safekeep_script: '/usr/local/sbin/safekeep-client.sh'
    
    # Send mail about backups to these email addresses
    safekeep_mail_to: [ 'backup' ]
    
    # Lists of paths, globs or regexps of files to exclude or include in backups
    safekeep_exclude_path: [ '/var/lock', '/var/run', '/var/tmp' ]
    safekeep_exclude_glob: [ '/home/*/tmp' ]
    safekeep_exclude_regexp: []
    
    safekeep_include_path: [ '/etc', '/home', '/opt', '/root', '/srv', '/usr/local', '/var' ]
    safekeep_include_glob: []
    safekeep_include_regexp: []




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.safekeep`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

