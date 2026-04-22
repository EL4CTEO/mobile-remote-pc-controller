# Remote PC Controller

Control your PC from your phone over Wi-Fi using a touch joystick, WASD keys, mouse clicks, and more.

## How It Works

- **Server** (`server/server.py`) runs on your PC — accepts WebSocket connections and translates them into mouse/keyboard actions via `pyautogui`.
- **Web App** (`web/index.html`) runs on your phone — sends touch input as WebSocket messages. Also buildable into an Android APK via Capacitor.

---

## Quick Start

### 1. Run the Server (PC)

```bash
cd server
pip install fastapi uvicorn pyautogui websockets
python server.py
```

The server prints your local IP on startup, e.g.:
```
==================================================
  Remote PC Controller Server
  Local IP: 192.168.1.100
  Connect your phone to: http://192.168.1.100:8765
==================================================
```

### 2. Connect from Your Phone

#### Option A: Browser (fastest)
Open `http://<YOUR_PC_IP>:8765` on your phone's browser. Add to home screen for fullscreen.

#### Option B: Install the APK
1. Go to the **Actions** tab of this repo
2. Download the latest `remote-pc-controller-debug` artifact
3. Transfer the APK to your phone and install it
4. Open the app, enter your PC's IP, and tap Connect

---

## Features

| Control | Action |
|---|---|
| Touch Joystick | Move mouse cursor |
| Left/Right Click | Mouse buttons |
| Middle Click | Middle mouse button |
| Scroll Up/Down | Mouse scroll |
| W A S D | Keyboard WASD |
| Arrow Keys | Keyboard arrows |
| SPC / ENT / ESC | Space, Enter, Escape |
| SHF / CTL / ALT / TAB / DEL | Modifier and special keys |

---

## Requirements

**Server (PC):**
- Python 3.8+
- `pip install fastapi uvicorn pyautogui websockets`

**Phone:**
- Any modern browser, or the built APK (Android 7+)
- Both devices on the same Wi-Fi network

---

## Project Structure

```
mobile-remote-pc-controller/
├── server/
│   └── server.py          # FastAPI WebSocket server
├── web/
│   ├── index.html          # Mobile-optimized SPA
│   ├── package.json        # Capacitor dependencies
│   └── capacitor.config.json
├── .github/workflows/
│   └── build-apk.yml       # CI: builds Android APK
└── README.md
```

## Notes

- Make sure your PC firewall allows port **8765**.
- The APK is a debug build — install at your own risk.
- For production use, consider signing the APK and using HTTPS/WSS.
