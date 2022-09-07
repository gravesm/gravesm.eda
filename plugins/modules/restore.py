#!/usr/bin/python


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.gravesm.eda.plugins.module_utils.client import AwsClient


ARG_SPEC = {
    "current_state": {"type": "dict"},
    "connection": {"type": "dict"},
    "event": {"type": "dict"},
}

def find_by_arn(arn, state):
    for k, v in state.items():
        if v.get("Properties", {}).get("Arn") == arn:
            return k, v

def main():
    module = AnsibleModule(argument_spec=ARG_SPEC)
    conn = module.params.get("connection") or {}
    client = AwsClient(**conn)
    event = module.params.get("event")
    name, resource = find_by_arn(event["Arn"], module.params.get("current_state", {}))
    if not resource:
        module.fail_json(changed=False, msg="Could not find resource")
    result = client.present(resource)
    module.exit_json(changed=True, resources={name: result})


if __name__ == "__main__":
    main()
