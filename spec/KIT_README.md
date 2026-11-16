# Project 4 (Inverse Kinematics) — student kit

Everything you need for Project 4, without the rest of the course repo.

**Dates:** released Mon Nov 9, 2026; the checkpoint is due Fri Nov 13, 2026, and the project is due
Wed Nov 18, 2026.

- **`docs/PROJECT4_*.md`**: start here. This is the assignment handout: overview, learning
  goals, the checkpoint ("Robot Jacobian Service"), the final requirements, and how you are graded.
- **`spec/IK_API.md`**: the exact contract. It covers the parameter server and
  `robot_description` (the same as in Project 3, restated in full), `/ik/robot_jacobian`, the one-step
  `/ik/solve_robot_step` (Jacobian transpose, and the Jacobian pseudoinverse, plain or damped), the full
  `/ik/solve_robot` (position and full pose), the frame everything is expressed in, and what
  `make run` must start.
- **`spec/ROBOT_DESCRIPTION.md`**: the URDF rules (the same as Project 3's, restated in full): which descriptions
  are valid, which elements and attributes are read, the defaults, and the kinematic
  conventions.
- **`spec/ROSBRIDGE_PROTOCOL.md`**: the course's TCP/JSON rosbridge protocol on `127.0.0.1:9095`,
  the same one your Project 1 gateway speaks. Your gateway must accept request lines of at least 1 MiB, and its
  service-call timeout must be longer than your slowest solve (see `spec/IK_API.md`).
- **`starter/`**: four alternative starting points (`c/`, `cpp/`, `python/`, `rust/`). Choose
  **one**. Each is a placeholder: a `Makefile` (`build`, `run`, `clean`, `test`), a `main`
  program that prints a `TODO` line, and a small example of reading a URDF with that language's
  bundled XML parser. The starters include no middleware and no nodes: bring your Project 1
  middleware and your Project 3 parameter server and URDF reader, and write the IK services
  yourself. See `starter/README.md`.
- **`make_submission.sh`**: once your chosen starter directory builds and runs, run
  `./make_submission.sh <c|cpp|python|rust>` (or `./make_submission.sh path/to/your/project` for
  a project you keep elsewhere) to produce a correctly shaped `submission.tar.gz`. Its `Makefile`
  is at the archive root, which is what the autograder expects. If your unzip tool dropped the
  execute bit, run it as `bash make_submission.sh ...`.

The kit ships no robot description. Start from the two-link arm in
`spec/ROBOT_DESCRIPTION.md` (its Jacobian is worked in full in `spec/IK_API.md`), then write
small URDFs of your own that cover what that one does not: a prismatic joint with a non-unit
axis, a fixed joint inside the chain, a branch off the chain, and a chain of more than six
movable joints. Real robots' published URDF files are valid descriptions too, under the rules of
`spec/ROBOT_DESCRIPTION.md`.
