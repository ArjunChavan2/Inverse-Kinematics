"""Example test: the Jacobian of the spec's worked two-link arm.

Copy this file to tests/test_<your name>.py to start a new test, then change
the robot, the request and the checks. Run it with `make test` while `make run`
is running in another terminal. See tests/README.md for the rules.
"""

import math
import time

from rosbridge_client import Rosbridge

URDF = """<robot name="two_link">
  <link name="base"/><link name="upper"/><link name="fore"/><link name="tip"/>
  <joint name="shoulder" type="revolute"><parent link="base"/><child link="upper"/>
    <axis xyz="0 0 1"/><limit lower="-3" upper="3"/></joint>
  <joint name="elbow" type="revolute"><parent link="upper"/><child link="fore"/>
    <origin xyz="1 0 0"/><axis xyz="0 0 1"/><limit lower="-3" upper="3"/></joint>
  <joint name="tip_mount" type="fixed"><parent link="fore"/><child link="tip"/>
    <origin xyz="1 0 0"/></joint>
</robot>
"""
REQUEST = {"joint_state": {"name": ["shoulder", "elbow"], "position": [0.0, math.pi / 2]}, "endeffector_frame": "tip"}

with Rosbridge() as ros:  # connects to your runtime on 127.0.0.1:9095
    loaded = ros.call_service("/param_server/set_param", {"name": "robot_description", "value": URDF})
    assert loaded["result"] is True, loaded
    version = loaded["values"]["version"]
    deadline = time.monotonic() + 3  # replies reflect a new description within 2 s
    while True:
        reply = ros.call_service("/ik/robot_jacobian", REQUEST)
        if reply["values"].get("description_version", 0) >= version or time.monotonic() > deadline:
            break
        time.sleep(0.1)

# The test passes if it ends normally. A failed assert fails it and shows
# its message, so include what you received.
assert reply["result"] is True, reply
assert reply["values"]["joint_names"] == ["shoulder", "elbow"], reply
expected = [[-1, 1, 0, 0, 0, 1], [-1, 0, 0, 0, 0, 1]]  # the spec's worked example
for got_row, want_row in zip(reply["values"]["jacobian"], expected):
    assert all(abs(g - w) <= 1e-4 for g, w in zip(got_row, want_row)), reply
