debops.debug
############


Dump all variables used by Ansible during playbook run to a file for
inspection. This role is not active during normal playbook operation and
should be used for development only.

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.debug




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # Where to save all Ansible variables
    debug_variables: '/tmp/ansible_variables'




Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.debug`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

