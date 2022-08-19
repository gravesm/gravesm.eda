# Event driven and declared state demo

This is a demo using the gravesm.eda collection. To use this, first, add whatever AWS resources you want to the `resources.yml` file. There's a role in there now, but you'll need to add a Principal to it. Then you'll need to configure your hosts.yml file. The `ansible_python_interpreter` should point to a python interpreter with `requirements.txt` installed into it. The `state_file` variable should also be set; this is where Ansible will store the current state of tracked resources. This also needs to be set in the `rules.yml` file.

Deploy the resources you defined with:

```
$ ansible-playbook deploy.yml -i hosts.yml
```

Then start up [ansible-events](https://github.com/benthomasson/ansible-events):

```
$ ANSIBLE_CONFIG=ansible.cfg ansible-events --rules rules.yml -i hosts.yml --env-vars ANSIBLE_CONFIG
```

This will create a named pipe called `ansible-events-queue` in the current directory by default (configurable in `rules.yml`). You can simulate an AWS event by writing to this pipe. An event should be a valid JSON object. This demo just looks for a top-level `Arn` property on the event, for example:

```
$ echo '{"Arn": "some-arn"}' > ansible-events-queue
```
