# Project 4 — Inverse Kinematics

EECS 367 Project 4 in Python (stdlib only): the Project 3 runtime (gateway, registry, `param_server`,
URDF reader, FK) plus three IK services on `127.0.0.1:9095`: `/ik/robot_jacobian` (checkpoint),
`/ik/solve_robot_step` and `/ik/solve_robot` (final).

```
make build   # py_compile src/*.py
make run     # gateway + param_server (+ IK services once registered in src/main.py)
make test    # tests/run_tests.py, with `make run` up in another terminal
make clean
sh make_submission.sh   # builds submission.tar.gz
```

- `src/jacobian.py`, `src/ik_step.py`, `src/ik_solve.py`, `src/ik_node.py` — IK stubs (docstrings describe the contract).
- `spec/` — course handout (`PROJECT4_IK.md`) and contracts (`IK_API.md`, `ROBOT_DESCRIPTION.md`, `ROSBRIDGE_PROTOCOL.md`).

Status: stubs only; nothing implemented yet.
