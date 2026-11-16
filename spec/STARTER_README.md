# Project 4 starter directories

This folder contains **four alternatives**, not one submission. Choose one: `python/`, `c/`,
`cpp/`, or `rust/`. Read `docs/PROJECT4_IK.md` first; it is the full assignment.

Each starter builds and runs as-is, but it does nothing useful yet. It gives you:

| Language | Where to start | Course-supplied XML parser (the same one as Project 3) |
|---|---|---|
| Python | `src/main.py`; `src/urdf_example.py` shows the XML plumbing | the standard library's `xml.etree.ElementTree` |
| C | `src/main.c`; `src/urdf_example.c` shows the XML plumbing | ezxml 0.8.6 in `third_party/ezxml/` (built by the `Makefile`) |
| C++ | `src/main.cpp`; `src/urdf_example.cpp` shows the XML plumbing | pugixml 1.14 in `third_party/pugixml/` |
| Rust | `src/main.rs` (`print_links` shows the XML plumbing) | roxmltree 0.20.0 in `vendor/roxmltree/` (a path dependency in `Cargo.toml`) |

The examples only read XML. The vendored parsers are unmodified upstream releases; their
licenses are next to their sources. You MAY replace them with your own parser, or reuse the
URDF reader you wrote for Project 3.

What the starters do **not** include is your middleware, your parameter server, or any node.
Bring your Project 1 rosbridge gateway and publish/subscribe layer and your Project 3 parameter
server, URDF reader and forward kinematics, write the three IK services `spec/IK_API.md`
describes (`/ik/robot_jacobian`, `/ik/solve_robot_step`, `/ik/solve_robot`), and extend the
`Makefile` so that `make build` compiles everything and `make run` starts the graded runtime
(gateway on `127.0.0.1:9095`, `param_server`, and whatever answers the IK services). How you
split this into files, classes, and processes is up to you. Two reminders from the handout:
your gateway and every node-to-node connection must accept lines of at least 1 MiB, and your
gateway's service-call timeout must be longer than your slowest solve.

There is no linear-algebra library in the course image: write the small matrix code you need
yourself (in the damped-least-squares step's `J Jᵀ` form, a 3×3 system, or 6×6 for a full pose).

**Rust and `serde_json`.** The course environment builds Rust offline from a fixed set of crates.
To use `serde_json`, add this line under `[dependencies]` in `Cargo.toml`:

```toml
serde_json = { version = "=1.0.151", features = ["float_roundtrip"] }
```

The set is `serde_json` 1.0.151 and the crates it needs: `serde`, `serde_core` and `serde_derive`
1.0.229, `itoa` 1.0.18, `memchr` 2.8.3, `zmij` 1.0.23, `proc-macro2` 1.0.107, `quote` 1.0.47,
`syn` 3.0.3 and `unicode-ident` 1.0.24. If you submit a `Cargo.lock`, it must list exactly these
versions: one that `cargo` wrote with network access may name newer ones, which do not resolve
offline. No other crate is available.

To submit, create `submission.tar.gz` from the **contents** of the one directory you chose, so
its `Makefile` is at the archive root. From the student kit's root, `./make_submission.sh
<python|c|cpp|rust>` does this for you. Do not submit this parent `starter/` directory.
