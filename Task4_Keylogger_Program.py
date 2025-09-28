# Simple input-logger (educational demo)
# This is NOT a background keylogger — it only logs lines you type and press Enter for.
log_file = "demo_input_log.txt"

print("Simple input logger. Type lines and press Enter. Type 'EXIT' to quit.")
while True:
    try:
        line = input()
    except EOFError:
        break
    if line.strip().upper() == "EXIT":
        break
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(line + "\n")

print("Stopped. Logs saved to", log_file)
