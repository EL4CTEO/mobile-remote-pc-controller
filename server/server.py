import asyncio
import json
import socket
import pyautogui
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import uvicorn
import os

app = FastAPI()

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

STATIC_DIR = os.path.join(os.path.dirname(os.path__), "web")


@app.get("/")
async def root():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return HTMLResponse(f.read())
    return HTMLResponse("<h1>Remote PC Controller</h1><p>Put index.html in the web/ folder.</p>")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)
            action = msg.get("action")

            if action == "move":
                dx = float(msg.get("dx", 0))
                dy = float(msg.get("dy", 0))
                pyautogui.moveRel(dx, dy, duration=0)

            elif action == "click":
                button = msg.get("button", "left")
                pyautogui.click(button=button)

            elif action == "scroll":
                dy = int(msg.get("dy", 0))
                pyautogui.scroll(dy)

            elif action == "key":
                key = msg.get("key", "")
                if key:
                    pyautogui.press(key)

            elif action == "key_down":
                key = msg.get("key", "")
                if key:
                    pyautogui.keyDown(key)

            elif action == "key_up":
                key = msg.get("key", "")
                if key:
                    pyautogui.keyUp(key)

    except WebSocketDisconnect:
        pass
    except Exception as e:
        print(f"Error: {e}")


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


if __name__ == "__main__":
    ip = get_local_ip()
    print(f"\n{'='*50}")
    print(f"  Remote PC Controller Server")
    print(f"  Local IP: {ip}")
    print(f"  Connect your phone to: http://{ip}:8765")
    print(f"{'='*50}\n")
    uvicorn.run(app, host="0.0.0.0", port=8765)
