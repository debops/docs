Installation
===========================

Installing Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

DebOps requires a dependency that is not already installed by Ansible.
Install ``netaddr`` however you see fit:

   $ apt-get install python-pip python-netaddr
   $ yum install python-pip python-netaddr
   $ pip install netaddr



Installing the DebOps scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The easiest way to install DebOps is::

   $ sudo pip install debops
   $ debops-update

If you dont have Ansible installed, the bootstrap-ansible.sh can do it 
for you::
   
   $ ./misc/scripts/bootstrap-ansible.sh v1.8.2

This installs version 1.8.2. Without version pin, the newest will be installed.

Other commonly used choices on how to install DebOps:

* Install the scripts into your own ``~/bin``::

   $ pip install --user debops
   $ debops-update


Updating the DebOps scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For updating the DebOps scripts run (assuming you used `sudo` when
installing)::

  $ sudo pip install -U --no-deps debops

..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
