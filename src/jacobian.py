"""Manipulator Jacobian of a chain (checkpoint: /ik/robot_jacobian). Owner-written, graded exercise.

Everything is in the root-link frame. Contract: spec/IK_API.md.
"""
from __future__ import annotations

from urdf import RobotModel


def chain_joints(model: RobotModel, endeffector: str) -> list:
    """Return the Joint objects on the path root -> endeffector, root first, fixed joints included.

    Joints on other branches are not part of the chain. Raise ValueError if endeffector is not a link.
    """
    raise NotImplementedError


def end_effector_pose(model: RobotModel, endeffector: str, positions: dict[str, float]) -> list[list[float]]:
    """Return the 4x4 pose of the endeffector link in the root frame (p_e is its translation, R_e its rotation).

    positions maps joint name -> q; movable joints it does not name are at 0, and values are never clamped.
    """
    raise NotImplementedError


def robot_jacobian(model: RobotModel, endeffector: str, positions: dict[str, float]) -> tuple[list[str], list[list[float]]]:
    """Return (joint_names, rows): the chain's movable joints root first, and one 6-vector row per joint.

    Row i is [v_x, v_y, v_z, w_x, w_y, w_z] for joint i, in the root frame, where p_i and R_i are the joint
    frame's origin and rotation (after its <origin>, before its motion) and p_e is the end-effector point:
      revolute/continuous: [z x (p_e - p_i); z] with z = R_i a / |a|
      prismatic:           [R_i a; 0, 0, 0]  with a as written (NOT normalized)
    This N x 6 layout is the transpose of the textbook 6 x N Jacobian. Never clamps q to the limits.
    """
    raise NotImplementedError
