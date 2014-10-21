debops-task
^^^^^^^^^^^

Wraps ``ansible``, it can accept anything ``ansible`` does.

You could use it to run adhoc tasks against your hosts.

::

    debops-task all -m setup

    debops-task somegroup -m shell "touch /tmp/foo && rm -rf /tmp/foo"

