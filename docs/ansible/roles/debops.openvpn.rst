debops.openvpn
###############

`debops.openvpn` role can be used to install and manage `OpenVPN`
configurations for multiple connections on both client- and
server-side.

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top


.. warning::

  **This is a beta role**, which means that it might be significantly
  changed in the future. Be careful while using this role in a
  production environment.

  If you are an experienced OpenVPN user, the author would appreciate
  your feedback and enhancements.



Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.auth


Example
~~~~~~~~~~~~~~

This is a (not working) example on how to set up a server and a
client. Most parameters will be written into the 

Server side::

  openvpn_generate_dh_param_file: True

  openvpn_connections:

  - name: Office Server
    server: 192.168.200.0 255.255.255.0
    dev: tun # routed tunnel

    cert: office-server.crt
    key: office-server.key  # This file should be kept secret

    route:
     - 10.10.0.0 255.255.0.0 10.1.1.1
     - 20.20.0.0 255.255.0.0 20.2.2.2 

    push:
     - ping 10
     - ping-restart 60


Client side::

  openvpn_generate_dh_param_file: False

  openvpn_connections:
  - name: Client Stefan
    client: True
    dev: tun # must match server side

    cert: client-stefan.crt
    key: client-stefan.key  # This file should be kept secret
    tls-remote: '/C=DE/ST=Bayern/O=Crazy_Compilers/CN=OpenVPN/emailAddress=openvpn@crazy-compilers.com'

    # See the openvpn documentation for `remote` and `connection`
    remote:
      - vpn1.example.com
      - vpn2.example.com 1193
    connection:
     - remote: 30.20.10.1 4321
     - remote: 192.70.78.2 1234
       http-proxy: 192.168.0.9 8080
       http-proxy-retry: 10
    http-proxy-options:
       VERSION: version
       AGENT: user-agent


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    # Using a Diffie-Hellman parameter size below 2048 is to be
    # considered insecure.
    openvpn_dh_param_size: 4096

    openvpn_generate_dh_param_file: True

    openvpn_default_options:
      user: nobody
      group: nobody
      persist-key: True  # required if user is not root
      persist-tun: True  # required if user is not root
      remote-random-hostname: True
      tun-ipv6: '{{ ansible_all_ipv6_addresses | bool }}'  # only valid if dev=tun
      verb: 3
      mute: 5
      ca: ca.crt
      dh: 'dh{{openvpn_dh_param_size}}.pem'
      cipher: AES-256-CBC
      comp-lzo: True
      proto: udp # this is the default anyway, but having the defined
                 # eases check
    
    openvpn_default_client_options:
      ns-cert-type: server
      resolv-retry: infinite
      nobind: True
    
    openvpn_default_server_options:
      ns-cert-type: client
      max-clients: 5
    
    openvpn_connections: []




Authors and license
~~~~~~~~~~~~~~~~~~~

`openvpn` role was written by:

- 'Hartmut Goebel' | [e-mail](mailto:'h.goebel@crazy-compilers.com) | [website](http://www.crazy-compilers.com)

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_


..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
