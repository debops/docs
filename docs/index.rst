.. DebOps documentation master file, created by
   sphinx-quickstart on Tue Oct 21 10:34:56 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


|debops_logo| `DebOps <http://debops.org>`_ documentation
=============================================================

**Your Debian-based data center in a box**

A collection of `Ansible <http://ansible.com/>`_ playbooks,
scalable from one container to an entire data center.

DebOps is a framework
---------------------

- **60+ highly extensible roles** with sane defaults
- **Tuned for production** and works great for development
- **Built for modularity** so extending it is simple
- **Custom scripts** to tie everything together

We believe in the UNIX philosophy; one tool should only do one thing very well.
DebOps has many playbooks and roles but it is just a set of focused tools to
help you run and manage your infrastructure.

In fact all of the DebOps playbooks and roles can be ran with Ansible directly.


Do you want to contribute?
--------------------------

DebOps itself is just a name, it's the sum of its parts. So we sincerly
welcome contributions!

* IRC: `#debops <http://webchat.freenode.net/?channels=debops>`_
* `Mailing list and Forum <https://groups.io/org/groupsio/debops>`_
* Issue reporting: `debops/debops issue tracker
  <https://github.com/debops/debops/issues>`_.
* Code submission: Please have a look at the
  :ref:`contributions page <contributing-guidelines>`

Contents:

.. toctree::
   :maxdepth: 2
   :glob:

   debops/docs/index
   installation
   getting-started
   creating-a-local-apt-server-to-use-backports
   service-ports
   using-linux-containers
   versions
   ansible/roles/index
   ansible/roles/ansible-*/docs/index


.. |debops_logo| image:: http://debops.org/images/debops-small.png

..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
