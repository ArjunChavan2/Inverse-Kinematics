"""IK service node: registers /ik/robot_jacobian, /ik/solve_robot_step and /ik/solve_robot on the Registry.

Owner-written. Wire it in main.py next to param_server.register(). Contract: spec/IK_API.md.
"""
from __future__ import annotations

from registry import Registry


def load_description(registry: Registry) -> tuple[object | None, int]:
    """Fetch robot_description via /param_server/get_param and return (RobotModel | None, version).

    Version is 0 when never set. If the newest description is invalid (urdf.parse_urdf raises ValueError),
    either return (None, that_version) to reject requests, or keep the previous valid robot; never crash.
    Must reflect a newly set description within 2 s (fetching per request satisfies this).
    """
    raise NotImplementedError


def parse_joint_state(model, endeffector: str, joint_state: dict) -> dict[str, float]:
    """Validate request["joint_state"] and return {movable joint name: position}.

    Raise ValueError for name/position length mismatch or a non-number (bool is not a number) position for a
    movable joint of the chain. Ignore names that are not movable joints; integers are accepted; never clamp.
    """
    raise NotImplementedError


def register(registry: Registry) -> None:
    """Register the three IK services. Every reply, success or error, carries values.description_version.

    Errors (no robot, unknown endeffector_frame, bad joint_state) reply result=False with a non-empty status
    and the service must keep answering afterwards. Solves can be slow: keep the gateway timeout above them.
    """
    raise NotImplementedError
