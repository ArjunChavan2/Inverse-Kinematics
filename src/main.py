"""Project 4 runtime entry point: gateway + param_server. IK services still TODO."""
from __future__ import annotations

import asyncio
import signal

import param_server
from gateway import Gateway, log
from registry import Registry


async def run() -> None:
    registry = Registry()
    param_server.register(registry)
    # TODO: register /ik/robot_jacobian, /ik/solve_robot_step, /ik/solve_robot
    gateway = Gateway(registry)
    await gateway.start()
    stop = asyncio.Event()
    for sig in (signal.SIGINT, signal.SIGTERM):
        asyncio.get_running_loop().add_signal_handler(sig, stop.set)
    await stop.wait()
    log("shutting down")
    await gateway.stop()


if __name__ == "__main__":
    asyncio.run(run())
