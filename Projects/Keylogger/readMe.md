# Keylogger using `pynput`

## Introduction

This Python script demonstrates how to create a simple keylogger using the `pynput` module. A keylogger is a program that records all the keystrokes made by a user on a keyboard. This script captures both alphanumeric and special keys, logs them to a list, and writes them to a file named `log.txt`.

## How It Works

1. **Keyboard Listener**: The script uses the `Listener` class from the `pynput.keyboard` module to monitor keyboard events. It listens for both key presses and key releases.
2. **Logging Keystrokes**: Each keystroke is captured and stored in a list, and then written to a file (`log.txt`).
3. **Stopping the Listener**: The keylogger continues capturing keystrokes until the `Esc` key is pressed, which stops the listener and ends the program.

## Dependencies

This script requires the `pynput` module. You can install it via `pip`:

```bash
pip install pynput
```
