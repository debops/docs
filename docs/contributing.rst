.. _contributing-guidelines:

Contributing Guidelines
=======================

- `Philosophy`_
- `Discussion`_
- `Issue reporting`_
    - `Scripts and documentation`_
    - `Playbooks and roles`_
    - `Tests`_
- `Code submissions`_
- `Code style`_
- `License agreement`_

Philosophy
^^^^^^^^^^

- Do one thing well
- Modularity and flexibility
- DebOps itself is just a name, it is the sum of its parts

Discussion
^^^^^^^^^^

Join us in `#debops <http://webchat.freenode.net/?channels=debops>`_ on Freenode
or post on the `debops-project <https://groups.google.com/forum/#!forum/debops-project>`_
mailing list.

Issue reporting
^^^^^^^^^^^^^^^

DebOps is officially hosted on Github at https://github.com/debops/debops.

Scripts and documentation
-------------------------

Checkout the `debops/debops issue tracker <https://github.com/debops/debops/issues>`_.

Playbooks and roles
-------------------

Checkout the `debops/debops-playbooks issue tracker <https://github.com/debops/debops-playbooks/issues>`_.

Tests
-----

Checkout the `debops/test-suite issue tracker <https://github.com/debops/test-suite>`_.

Code submissions
^^^^^^^^^^^^^^^^

We accept `pull requests <https://help.github.com/articles/using-pull-requests>`_
on everything. Here's a quick work flow:


1. Fork it into your Github account (https://github.com/debops/debops/fork)
2. Clone your fork onto your workstation::

     git clone git@github.com:YOURACCOUNT/debops.git

3. Create your feature branch (``git checkout -b my-new-feature``)
4. Commit your changes (``git commit -am 'Add some feature'``)

   Please try your best to make great commit messages. Have a read
   through `better commits
   <http://web-design-weekly.com/2013/09/01/a-better-git-commit>`_ and
   research how to use ``git add -p``.

5. Push to the branch (``git push origin my-new-feature``)

6. Submit your pull request through Github: Select the branch on your
   repo, click the green PR button and submit it.

7. (Optional) Keep in sync with development in the official repo:

   a. Add the official repo as your `upstream`::

         git remote add upstream https://github.com/debops/debops

   b. Update your fork::

        git checkout master # or whatever the main PR branch is for that repo
        git fetch upstream
        git rebase upstream/master
        git push origin master

      You should do this before making any commits and after your pull
      request has been accepted.


Code style
^^^^^^^^^^

For everything:

- Try your best to stay under 80 characters but don't go crazy trying
- 2 space indentation for everything unless noted otherwise
- Comments and output start with a capital letter and have no periods

For just yaml:

- Prefer ``role_foo`` and ``role_bar`` to using a ``role`` dictionary
- Use the multi-line style whenever possible (we're working on migrating to that)

License agreement
^^^^^^^^^^^^^^^^^

By contributing you agree that these contributions are your own
(or approved by your employer) and you grant a full, complete, irrevocable
copyright license to all users and developers of the project, present and
future, pursuant to the license of the project.

..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
