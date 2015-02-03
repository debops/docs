.. _configuration:

Configuration
=======================

**Note** You do not need to configure anything to run DebOps.

DebOps reads configuration files at several places. All configurations
files found are merged where the values read later take precedence.

Windows:

  | %APPDATA%\debops.cfg (with %APPDATA% defaulting to ~\Application Data)
  | `project-dir`\.debops.cfg

OS X:

  | ~/Library/Application Support/\debops.cfg
  | `project-dir`/.debops.cfg

All Others (including Linux):

  | /etc/debops.cfg
  | In each `dir` of $XDG_CONFIG_DIRS: `dir`/debops.cfg
  | $XDG_CONFIG_HOME/debops.cfg
  | `project-dir`/.debops.cfg


Configuration File Format
----------------------------


The configuration file are simple `INI-files
<https://en.wikipedia.org/wiki/INI_file>`_. Supported sections and
values are:


+--------------+----------------+-----------------------------------------------+
| section      | item           | default                                       |
+==============+================+===============================================+
|paths         |data-home       | | $XDG_DATA_HOME/debops (Unix/Linux)          |
|              |                | | %APPDATA%\debops  (Windows)                 |
|              |                | | ~/Library/Application Support\debops (OS X) |
+              +----------------+-----------------------------------------------+
|              |install-path    | %(data-home)s/debops-playbooks                |
+              +----------------+-----------------------------------------------+
|              |playbooks-paths | %(install-path)s/playbooks                    |
+--------------+----------------+-----------------------------------------------+
|ansible `XXX` | Items defined here are going into section `XXX` of             |
|              | ansible.cfg.                                                   |
+--------------+----------------------------------------------------------------+


..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
