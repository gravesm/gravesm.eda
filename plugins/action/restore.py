import copy
import json

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        super().run(tmp, task_vars)
        module_args = copy.deepcopy(self._task.args)

        try:
            state_file = task_vars.get("state_file")
            with open(state_file) as fp:
                current_state = json.load(fp)
        except Exception:
            current_state = {}

        module_args["current_state"] = current_state
        module_args["event"] = task_vars.get("event")
        return self._execute_module(
            module_name=self._task.action, module_args=module_args, task_vars=task_vars
        )
