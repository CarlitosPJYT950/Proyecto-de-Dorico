# WebSocket Chat Backend

This directory contains a simple Python WebSocket chat server.

## Quick start

### 1) Activate the virtual environment

- **Windows (PowerShell)**

```powershell
cd .vscode/api
.\.venv\Scripts\Activate.ps1
```

- **Windows (cmd.exe)**

```cmd
cd .vscode/api
.\.venv\Scripts\activate.bat
```

- **macOS/Linux**

```sh
cd .vscode/api
source .venv/bin/activate
```

### 2) Run the server

```sh
python server.py
```

### 3) Connect clients

Connect any WebSocket client to:

```
ws://localhost:8765
```

Each message sent by any client is broadcast to all connected clients.

## Notes

- No authentication is provided.
- The server is intentionally minimal; extend it as needed (user names, rooms, persistence, etc.).
