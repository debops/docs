Installation
===========================

Installing Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

DebOps requires a dependency that is not already installed by Ansible.
Install ``netaddr`` however you see fit::

   $ apt-get install python-pip python-netaddr
   $ yum install python-pip python-netaddr
   $ pip install netaddr



Installing the DebOps scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The easiest way to install DebOps is::

   $ sudo pip install debops
   $ debops-update

If you don't have Ansible installed, the script
``bootstrap-ansible.sh`` can do it for you::
   
   $ ./misc/scripts/bootstrap-ansible.sh v1.8.2

This installs version 1.8.2. Without version pin, the newest version
will be installed.


Other commonly used choices on how to install DebOps:

* Install the scripts into your own ``~/bin``::

   $ pip install --user debops
   $ debops-update

For more installation options please have a look at the `pip User Guide
<https://pip.pypa.io/en/latest/user_guide.html>`_.


Installing the current development version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to install the current development version of DebOps,
choose one off::

  $ sudo pip install https://github.com/debops/debops/archive/master.zip


If you want to help working on DebOps, it's best to check out the
scripts from github::

  $ git clone https://github.com/debops/debops ~/my-projects/debops
  $ cd ~/my-projects/debops

You can still install the scripts so you can use them easily, e.g.::

   $ pip install --user ~/my-projects/debops
   $ debops-update


Updating the DebOps scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For updating the DebOps scripts run (assuming you used `sudo` when
installing)::

  $ sudo pip install -U --no-deps debops


If you installed the development version of DebOps and want to update
it, simply use::

  $ sudo pip install -U --no https://github.com/debops/debops/archive/master.zip


..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
