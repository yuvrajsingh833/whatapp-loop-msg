# WhatsApp Auto Messenger using PyAutoGUI

This Python script automates the process of sending repetitive WhatsApp messages to a specific contact using **WhatsApp Web** and the `pyautogui` library.

> ⚠️ **Note:** This script is intended for educational or testing purposes only. Use responsibly and avoid spamming or violating WhatsApp's terms of service.

---

## 📋 Features

- Sends messages automatically to a given WhatsApp number.
- Uses the **same WhatsApp Web tab** without opening new ones.
- Sends messages at a set interval (1 second in this case).
- Useful for testing or controlled automation tasks.

---

## 🚀 Requirements

- Python 3.x
- Installed Python packages:
  - `pyautogui`
  - `webbrowser` (built-in)
  - `time` (built-in)

### Install Dependencies

```bash
pip install pyautogui
```

---

### 🧠 How It Works

- Opens WhatsApp Web in the default browser for the given phone number.
- Waits 10 seconds to allow the page and chat to load.
- Sends the specified message 1000 times with a 1-second delay between each.

---

### 📝 How to Run

1. **Edit the Script**: Replace the phone number with your desired contact number in international format (with + and country code).
2. **Open WhatsApp Web**: Make sure you are logged in and WhatsApp Web is active.
3. **Run the Script**:

> ⚠️ **Note:** Make Sure that the Present working directory of the terminal should be the same folder in which the python file is presnet eg. whatsapp_loop.py .

```bash
python whatsapp_loop.py
```

---

## 👤 Author

**Yuvraj Singh Rathore**  
GitHub: [yuvrajsingh833](https://github.com/yuvrajsingh833)  
Email: yuvrajsingh1034@gmail.com

---

## ⚠️ Disclaimer

This script can be disruptive if misused. Do not:

- Spam individuals or groups.
- Use it for harassment or abuse.

You are solely responsible for how you use this script.

Made by Yuvraj Singh Rathore with ❤️
