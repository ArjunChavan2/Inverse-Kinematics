"""One gradient-descent IK step (/ik/solve_robot_step) and the small linear algebra it needs. Owner-written.

Stateless: the result depends only on the arguments. No numpy; write the linear solve yourself.
"""
from __future__ import annotations


def solve_linear(A: list[list[float]], b: list[float]) -> list[float]:
    """Solve A x = b by Gaussian elimination with partial pivoting (A is n x n, typically 3x3 or 6x6).

    Raise ValueError if A is singular (e.g. undamped pseudoinverse on a planar arm).
    """
    raise NotImplementedError


def orientation_error(R_target: list[list[float]], R_e: list[list[float]]) -> list[float]:
    """Return the rotation vector (axis * angle, angle in [0, pi]) of R_target * R_e^T, in the root frame.

    Zero vector when the angle is 0; a valid axis with magnitude pi when the angle is pi.
    """
    raise NotImplementedError


def quat_to_matrix(x: float, y: float, z: float, w: float) -> list[list[float]]:
    """Rotation matrix of the unit quaternion (x, y, z, w), w the scalar part (formula in spec/IK_API.md)."""
    raise NotImplementedError


def solve_step(rows: list[list[float]], error: list[float], method: str, step_length: float, damping: float) -> list[float]:
    """Return delta_q, one entry per row of `rows` (the N x 6 Jacobian from jacobian.robot_jacobian).

    error is e (3 values, position only; use only the first 3 entries of every row) or [e; e_w] (6 values).
      "JacobianTranspose":     dq = alpha * J^T e
      "JacobianPseudoinverse": dq = alpha * J^T (J J^T + lambda^2 I)^-1 e   (lambda = 0 is the plain pseudoinverse)
    Note lambda is squared. Raise ValueError for an unknown method.
    """
    raise NotImplementedError
