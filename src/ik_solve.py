"""Full IK solve (/ik/solve_robot): iterate the step until within tolerance or out of iterations. Owner-written."""
from __future__ import annotations

from urdf import RobotModel


def solve_robot(model: RobotModel, request: dict) -> dict:
    """Iterate from request["joint_state"] toward request["endeffector_pose"]; return the reply `values`.

    Loop: measure position error |p_target - p_e| (and, unless ik_position_only, the orientation angle of
    R_target^T R_e). If both are below their tolerances stop with converged=True; if max_iterations steps were
    taken stop with converged=False; else take one ik_step.solve_step, then clamp every revolute and
    prismatic joint to its limits (continuous joints are unlimited), and repeat.

    Returns {"configuration_solution": {name, position}, "converged": bool,
             "final_error": {"position": m, "orientation": rad | None}, "iterations": int}.
    Honesty: converged and final_error describe the configuration RETURNED, not the one before the last step.
    An unreachable target is a normal converged=False reply, not an error.
    """
    raise NotImplementedError
