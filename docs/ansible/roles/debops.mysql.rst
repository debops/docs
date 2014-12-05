debops.mysql
############


Install and manage a MySQL database. At the moment only database on
``localhost`` is supported.

You can use this role as a dependency of another role to easily create
databases and users for a particular application (database and user
management is also available using Ansible inventory).

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.mysql


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.ferm``
- ``debops.secret``
- ``debops.tcpwrappers``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # ---- MySQL server configuration ----
    
    # Bind address of mysqld. If you want to allow access to the server over the
    # network, change this to '0.0.0.0' (for all interfaces) or for specific IP
    # address to bind on
    mysql_mysqld_bind_address: 'localhost'
    
    # Default mysqld port to listen on
    mysql_mysqld_port: 3306
    
    # This is a list of IP addresses or CIDR networks allowed to connect to MySQL
    # server from remote hosts. It will be applied in firewall (ferm) and
    # /etc/hosts.allow (tcpwrappers).
    # You will need to set mysql_mysqld_bind_address to 0.0.0.0 and restart MySQL
    # server for it to listen on all network interfaces.
    mysql_mysqld_allow: []
    
    # Maximum number of allowed connections
    mysql_mysqld_max_connections: 100
    
    # Use this hash variable to set additional mysqld options
    mysql_mysqld_options: {}
    #  'key_buffer': '16M'
    #  'skip-name-resolve':
    
    
    # ---- PHPMyAdmin support ----
    
    # Enable PHPMyAdmin? It will be installed on localhost with php5-fpm and nginx
    # See 'phpmyadmin' role for more configuration options
    mysql_phpmyadmin: False
    
    
    # ---- automysqlbackup configuration ----
    
    # Mail address to send messages to (account or alias name will be properly
    # routed by the Postfix SMTP server)
    mysql_backup_mailaddr: 'backup'
    
    # Specify the day of the week to create weekly backups (1 - Monday, 7 - Sunday)
    mysql_backup_doweekly: '6'
    
    # Don't keep copies of most recent backups by default
    mysql_backup_latest: 'no'
    
    
    # ---- MySQL databases and user accounts ----
    
    # List of MySQL databases to manage
    mysql_databases: []
      #- name: 'database_name'
      #  state: 'present,absent'        # optional
    
    # Length of randomly generated passwords (it's a string)
    mysql_password_length: '20'
    
    # Password for MySQL root user
    mysql_root_password: "{{ lookup('password', secret + '/credentials/' + ansible_fqdn + '/mysql/root/password length=' + mysql_password_length) }}"
    
    # List of MySQL users to manage (defaults first)
    mysql_users: []
      #- name: 'user_name'              # required
      #  host: 'localhost'
      #  state: 'present,absent'
      #  password: ''                   # if not specified, random will be generated
      #                                 # and saved in the 'secret' storage
      #  priv: 'user_name.*:ALL'
      #  append_privs: 'no,yes'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.mysql`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

