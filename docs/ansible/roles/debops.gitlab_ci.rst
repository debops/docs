debops.gitlab_ci
################



`GitLab CI`_ is a continuous integration service based around `GitLab`_. It
uses a GitLab instance for authentication and access to git repositories
(can be managed using ``debops.gitlab`` role) and `GitLab CI Runner`_
service to run the tests (can be installed using
``debops.gitlab_ci_runner`` role).

.. _GitLab CI: https://about.gitlab.com/gitlab-ci/
.. _GitLab: https://about.gitlab.com/
.. _GitLab CI Runner: https://github.com/gitlabhq/gitlab-ci-runner/

.. contents:: Table of Contents
   :local:
   :depth: 2
   :backlinks: top

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.gitlab_ci


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.etc_services``
- ``debops.redis``
- ``debops.nginx``
- ``debops.mysql``
- ``debops.ruby``
- ``debops.secret``
- ``debops.postgresql``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # ---- Basic options ----
    
    # Should GitLab CI role manage it's own dependencies (database, web server)?
    gitlab_ci_dependencies: True
    
    # What version of GitLab CI to install / manage
    gitlab_ci_version: '5.0'
    
    # Allow automatic upgrades to next version? If not, Ansible will stop execution
    # when it detects that GitLab CI requires upgrade
    gitlab_ci_auto_upgrade: True
    
    
    # ---- GitLab CI instance configuration ----
    
    # What database to use for GitLab CI instnce? Choices: mysql, postgresql
    gitlab_ci_database: 'mysql'
    
    # List of GitLab instances to include in login form
    gitlab_ci_urls:
      - 'https://code.{{ ansible_domain }}'
    
    # Domain which will be used for nginx server
    # GitLab CI will be configured with HTTPS enabled by default
    gitlab_ci_domain: [ 'ci.{{ ansible_domain }}' ]
    
    # E-mail sender name used by GitLab CI
    gitlab_ci_email_name: 'GitLab CI'
    
    # E-mail address used by GitLab CI
    gitlab_ci_email_from: 'gitlab-ci@{{ ansible_domain }}'
    
    # E-mail address for GitLab CI support
    gitlab_ci_email_support: 'root@{{ ansible_domain }}'
    
    
    # ---- Internal application settings ----
    
    # Patch GitLab CI source
    gitlab_ci_patch: True
    
    # Connection type for PostgreSQL database (choices: socket, port)
    gitlab_ci_postgresql_database_connection: 'socket'
    
    # nginx client_max_body_size value
    gitlab_ci_nginx_client_max_body_size: '5m'
    
    # nginx - gitlab proxy timeout in seconds
    gitlab_ci_nginx_proxy_timeout: '300'
    
    # unicorn connection timeout in seconds
    gitlab_ci_unicorn_timeout: '30'

List of internal variables used by the role::

    gitlab_ci_status_installed
    gitlab_ci_database_password
    gitlab_ci_postgresql_database_password
    gitlab_ci_status_upgrade


Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.gitlab_ci`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

