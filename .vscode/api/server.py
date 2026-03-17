r"""Simple WebSocket chat server.

Run this server and connect using any WebSocket client (browser, CLI, etc.).

Each message received is broadcast to all connected clients.

Run:
  - Windows (PowerShell):  .venv\Scripts\Activate.ps1; python server.py
  - Windows (cmd.exe):     .venv\Scripts\activate.bat && python server.py
  - Linux/macOS:           source .venv/bin/activate && python server.py

Then connect clients to ws://localhost:8765
"""

import asyncio
import logging
from typing import Any, Set

import websockets

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

CONNECTED: Set[Any] = set()


async def broadcast(message: str) -> None:
    """Send a message to all connected clients."""
    if not CONNECTED:
        return

    await asyncio.gather(
        *[ws.send(message) for ws in CONNECTED if ws.open],
        return_exceptions=True,
    )


async def handler(ws: Any, path: str) -> None:
    """Handle a connected WebSocket client."""
    CONNECTED.add(ws)
    logging.info("Client connected (%d total)", len(CONNECTED))
    try:
        async for message in ws:
            logging.info("Received: %s", message)
            await broadcast(message)
    except websockets.exceptions.ConnectionClosedOK:
        pass
    except websockets.exceptions.ConnectionClosedError as exc:
        logging.warning("Connection closed with error: %s", exc)
    finally:
        CONNECTED.discard(ws)
        logging.info("Client disconnected (%d total)", len(CONNECTED))


async def main() -> None:
    port = 8765
    host = "0.0.0.0"

    logging.info("Starting websocket chat server on ws://%s:%d", host, port)

    async with websockets.serve(handler, host, port):
        # Keep running until interrupted
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
