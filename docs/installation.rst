Installation
===========================

Installing Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^

DebOps requires a dependency that is not installed by Ansible. Install
``netaddr`` however you see fit::

   $ apt-get install python-netaddr
   $ yum install python-netaddr
   $ pip install netaddr
   $ easy_install netaddr


Installing the DebOps scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Download and install the scripts. As long as there is no release with
a officially declared version number we suggest cloning the git
repository. This makes it easy to update later::

   $ git clone https://github.com/debops/debops
   $ cd debops

Choose, who you want DebOps to be installed:

* System-wide into /usr/local::

     sudo make install

* System-wide into /opt/debops:
  This would allow passing ownership of
  the installation to some DebOps-operator. Mind to include
  ``/opt/debops/bin`` into your ``PATH``.

  ::

     sudo PREFIX=/opt/debops make install
     sudo chown -R debops:debops /opt/debops

* Scripts into /usr/bin, playbooks and roles into $HOME: This has the
  advantage that every user can have her own set of roles and
  playbooks.

  ::

    sudo make install-scripts
    debops-update

..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
