debops.apt_preferences
######################


`APT preferences`_ can be used to influence package selection performed by
APT during installation or upgrades.  You can for example tell APT that you
prefer packages from certain repositories or want to hold a package on
a particular version no matter what (among other things).

By default, if you don't specify version or provide custom pin configuration,
``debops.apt_preferences`` role will configure specified packages to be installed from
backports repository of a current OS release.

.. _APT preferences: https://wiki.debian.org/AptPreferences

.. contents:: Table of Contents
   :local:
   :depth: 3
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.apt_preferences




Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory:

.. py:function:: apt_preferences_list(list)

   List of apt_preferences(5) pins to configure in ``/etc/apt/preferences.d/``.
   These pins will be configured on all hosts in the cluster, if set in
   ``inventory/group_vars/all/``.

   :param str  package:   Name(s) of the packages to include in this pin
   :param list backports: If present, this pin defines a preference for
                          backported package. You can specify names of OS
                          distributions on which this backport pin should be
                          enabled
.. py:function:: apt_preferences_group_list(list)

   List of apt_preferences(5) pins to configure in ``/etc/apt/preferences.d/``.
   These pins will be configured on hosts in a specified group, if set in
   ``inventory/group_vars/group_name/``. Only one group "level" is supported.

   :param str  package:   Name(s) of the packages to include in this pin
   :param list backports: If present, this pin defines a preference for
                          backported package. You can specify names of OS
                          distributions on which this backport pin should be
                          enabled

.. py:function:: apt_preferences_host_list(list)

   List of apt_preferences(5) pins to configure in ``/etc/apt/preferences.d/``.
   These pins will be configured on specific hosts, if set in
   ``inventory/host_vars/host_name/``.

   :param str  package:   Name(s) of the packages to include in this pin
   :param list backports: If present, this pin defines a preference for
                          backported package. You can specify names of OS
                          distributions on which this backport pin should be
                          enabled

.. py:function:: apt_preferences_dependent_list(list)

   List of apt_preferences(5) pins to configure in ``/etc/apt/preferences.d/``.
   This variable is meant to be used from a role dependency in
   ``role/meta/main.yml``.

   :param str  package:   Name(s) of the packages to include in this pin
   :param list backports: If present, this pin defines a preference for
                          backported package. You can specify names of OS
                          distributions on which this backport pin should be
                          enabled

.. py:function:: apt_preferences_priority_default(str)

   Default pin priority used, if custom priority is not specified in a pin definition.
   By default, ``'500'``.

.. py:function:: apt_preferences_priority_version(str)

   Default pin priority used if custom priority is not specified in
   a versioned pin definition. By default, ``'500'``.


Detailed usage guide
~~~~~~~~~~~~~~~~~~~~

Each pin should be defined as a hash in one of above ``apt_preferences_*_list``
lists. All variables except ``item.package`` are optional, role will try to make
sensible choices if specific variables are not present.

- ``item.package``: string of package names affected by this pin, each
  package separated by space. You can use ``package-*`` wildcard to specify
  multiple packages. First package name will be included in automatically
  generated filename of the pin preferences file.

- ``item.backports``: list of OS releases which should be considered when
  ``debops.apt_preferences`` role configures pin for a backported package.
  If current OS release is not on this list, pin won't be created, and
  existing pin will be removed. This should allow for easy transition to
  next OS release.

- ``item.version``: specify a particular package version you want to pin,
  for exmple ``5.10``. It will be configured with added ``*`` at the end to
  allow for upgrades. By default versioned pins are set with priority
  ``1001``, which should ensure that selected pckage version is never
  upgraded, or it will be downgraded if required.

- ``item.priority``: specify custom priority for a pin. By default pins are
  created with priority ``500`` to allow for easy installation of packages
  from backports, versioned pins are created with priority ``1001``.

- ``item.reason``: a short description explaining the reason for a pin.
  Might be used to point a system administrator to useful documentation
  explaining why a particular pin is defined.

- ``item.filename``: name of the generated file with pin preferences, saved
  in ``/etc/apt/preferences.d/``. If undefined, ``debops.apt_preferences``
  role will automatically generate a filename.

- ``item.suffix``: additional string added at the end of autogenerated
  filename, can be used to prevent filename collisions.

- ``item.by_role``: name of a role which sets a particular pin. This name
  will be included in the autogenerated filename.

- ``item.pin``: custom pin definition. If this variable is undefined,
  ``debops.apt_preferences`` role will automatically configure selected
  packages with preference for a backported version.

- ``item.raw``: instead of generating a pin automatically, use contents of
  this text block for pin configuration. Might be used to create several
  pins in one file.

- ``item.delete``: if this variable is defined and ``True``, preferences
  file for this pin will be deleted and new one will not be created.

Usage examples
==============

This role can be used directly from a playbook, with pin configuration
specified directly:

::

    ---
    - name: Install nginx from wheezy-backports on Wheezy
      hosts: all
      sudo: True
      roles:
         - role: debops.apt_preferences
           tags: apt_preferences
           apt_preferences_list:
             - package: 'nginx nginx-*'
               backports: [ 'wheezy' ]
      tasks:
        - apt: name=nginx state=latest

More fine-grained configuration can be specified using inventory variables, for
example per group or per host:

::

    ---
    apt_preferences_group_list:
      - package: '*'
        suffix: '_testing'
        pin: 'release a=testing'
        priority: '900'
        reason: 'Prefer packages from testing'
    
      - package: '*'
        suffix: '_debian'
        pin: 'release o=Debian'
        priority: '-10'
        reason: 'Lower package preference from other releases'

You can also use ``debops.apt_preferences`` as a dependency in another role:

::

    ---
    dependencies:
      - role: debops.apt_preferences
        tags: apt_preferences
        apt_preferences_dependent_list:
          - package: 'mysql-server mysql-client mysql-common'
            version: '5.5'
            by_role: 'debops.mysql'
            reason: 'Hold mysql on version 5.5*'


Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.apt_preferences`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

