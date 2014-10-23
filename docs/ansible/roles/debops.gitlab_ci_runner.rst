debops.gitlab_ci_runner
#######################

|Travis CI| |test-suite| |Ansible Galaxy|

.. |Travis CI| image:: http://img.shields.io/travis/debops/ansible-gitlab_ci_runner.svg?style=flat
   :target: http://travis-ci.org/debops/ansible-gitlab_ci_runner

.. |test-suite| image:: http://img.shields.io/badge/test--suite-ansible--gitlab__ci__runner-blue.svg?style=flat
   :target: https://github.com/debops/test-suite/tree/master/ansible-gitlab_ci_runner/

.. |Ansible Galaxy| image:: http://img.shields.io/badge/galaxy-debops.gitlab_ci_runner-660198.svg?style=flat
   :target: https://galaxy.ansible.com/list#/roles/1568



`GitLab CI Runner`_ is a helper Ruby program which is used by `GitLab CI`_
service to run continuous integration tests. It should be installed on
a separate host (or multiple hosts) or even in a LXC or OpenVZ container
and is designed to be easily reinstalled if necessary. You will need
a GitLab CI instance to use Runners, which can be installed and configured
using ``debops.gitlab_ci`` role.

.. _GitLab CI Runner: https://github.com/gitlabhq/gitlab-ci-runner/
.. _GitLab CI: https://about.gitlab.com/gitlab-ci/

Installation
~~~~~~~~~~~~

This role requires at least Ansible ``v1.7.0``. To install it, run::

    ansible-galaxy install debops.gitlab_ci_runner


Role dependencies
~~~~~~~~~~~~~~~~~

- ``debops.ruby``
- ``debops.ansible``
- ``debops.postgresql``
- ``debops.mysql``
- ``debops.nodejs``


Role variables
~~~~~~~~~~~~~~

List of default variables available in the inventory::

    ---
    
    # ---- Runner configuration ----
    
    # URL of GitLab CI instance where this runner will try to register
    gitlab_ci_runner_url: 'https://ci.{{ ansible_domain }}'
    
    # Runner registration token (required). Currently there is no way to get this
    # token automatically. You should install GitLab CI instance and after login go
    # to Runners page, where you can find the token. Copy it and save in your
    # inventory.
    gitlab_ci_runner_token: ""
    
    # What version of GitLab CI to install / manage
    gitlab_ci_runner_version: '5.0'
    
    # Allow automatic upgrades to next version? If not, Ansible will stop execution
    # when it detects that GitLab CI requires upgrade
    gitlab_ci_runner_auto_upgrade: True
    
    # Number of runner threads to start by default
    gitlab_ci_runner_threads: '{{ ansible_processor_cores }}'
    
    
    # ---- CI environment ----
    
    # List of DebOps roles to run before gitlab_ci_runner. Currently available:
    # ansible, nodejs, mysql, postgresql
    gitlab_ci_runner_dependencies: []
    
    # List of Debian packages to install after runner has been configured
    gitlab_ci_runner_packages: []
    
    # Should gitlab-ci-runner user have full sudo access?
    gitlab_ci_runner_sudo: False
    
    # Configuration for MySQL database server. Runner will have access to databases
    # with defined prefix, for example 'ci_test_01'
    gitlab_ci_runner_mysql_user: 'gitlab-ci-runner'
    gitlab_ci_runner_mysql_password: '{{ gitlab_ci_runner_mysql_user }}'
    gitlab_ci_runner_mysql_database_prefix: 'ci_test'

List of internal variables used by the role::

    gitlab_ci_runner_status_installed
    gitlab_ci_runner_status_upgrade
    gitlab_ci_runner_status_registered


Authors and license
~~~~~~~~~~~~~~~~~~~

``debops.gitlab_ci_runner`` role was written by:

- Maciej Delmanowski | `e-mail <mailto:drybjed@gmail.com>`__ | `Twitter <https://twitter.com/drybjed>`__ | `GitHub <https://github.com/drybjed>`__

License: `GPLv3 <https://tldrlegal.com/license/gnu-general-public-license-v3-%28gpl-3%29>`_

