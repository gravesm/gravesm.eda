import json
import os

import aiofiles


def arn_in(arn, state):
    for k, v in state.items():
        if v.get("Properties", {}).get("Arn") == arn:
            return True


async def main(queue, args):
    state_file = args.get("state_file", "state.json")
    fifo = args.get("queue", "/tmp/ansible-events-queue")
    with open(state_file) as f:
        state = json.load(f)
    while True:
        try:
            os.mkfifo(fifo)
        except FileExistsError:
            os.unlink(fifo)
            os.mkfifo(fifo)
        async with aiofiles.open(fifo) as f:
            async for event in f:
                e = json.loads(event)
                if arn_in(e.get("Arn"), state):
                    await queue.put(json.loads(event))
