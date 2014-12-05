debops.etc_services
###################


``debops.etc_services`` role can be used to "reserve" or "register"
a service port in ``/etc/services`` file. Service ports configured this way
can appear as named entries in many command outputs, such as
``iptables -L`` or ``netstat -lp``.  You can also have convenient database
of reserved and free ports on a particular host, and reference ports by
their names in firewall configuration files.

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.etc_services




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Enable /etc/services.d/ support?
    etc_services: True
    
    # Name of diverted /etc/services, do not change if diversion is active!
    etc_services_diversion: '/etc/services.d/10_debian_etc_services'
    
    
    # ---- Local services ----
    
    # These lists allow you to generate entries for local services not included in
    # officially distributed /etc/services file. They will generate separate files
    # for each configured service in /etc/services.d/ which then will be assembled
    # into complete /etc/services file.
    
    # List of known parameters:
    #  - name: ''                      name of the service, required
    #  - port: ''                      port on which service is accessed, required
    #  - protocols: [ 'tcp','udp' ]    list of protocols to generate, optional
    #  - protocol: ''                  legacy protocol name to use, deprecated
    #  - comment: ''                   comment to add to the service entry, optional
    #  - filename: ''                  use this filename instead of a generated one
    
    # These lists should be used in inventory
    etc_services_list: []
    etc_services_group_list: []
    etc_services_host_list: []
    
    # This list can be used in a dependency variables for 'etc_services' role
    etc_services_dependency_list: []       # deprecated
    etc_services_dependent_list: []
    
      # Example entry
      #- name: 'servicename'
      #  port: '12345'
      #  protocols: [ 'tcp', 'udp' ]
      #  porotol: 'tcp'                    # deprecated
      #  comment: 'Example service'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.etc_services`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

