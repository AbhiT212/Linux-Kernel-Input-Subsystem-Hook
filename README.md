Here is the complete, concise, and professional `README.md`.

---

# Linux Kernel Input Notification Module

## Project Overview

This project implements a Loadable Kernel Module (LKM) that interfaces directly with the Linux keyboard notification chain. It captures hardware interrupt events (scancodes) at the kernel level and logs them to the kernel ring buffer. A companion user-space Python application parses this stream in real-time to reconstruct the input data.

## Disclaimer

**Educational Use Only:** This software was developed solely for research purposes to study Linux kernel subsystems and device driver architecture. It is not intended for malicious use or unauthorized surveillance. The author assumes no liability for misuse.

## Features

* **Kernel Space:** Hooks into `keyboard_notifier_list` to capture keystrokes in atomic context.
* **User Space:** Decodes raw scancodes from `dmesg` into human-readable ASCII.
* **Safety:** Uses non-blocking execution to maintain system stability.
* **Automation:** Includes a single-command build and execution script.

## Prerequisites

* Linux Kernel 5.x or newer
* GCC and Make
* Python 3.6+
* Root privileges

## Quick Start

To compile, load, and run the project with a single command:

```bash
chmod +x run.sh
sudo ./run.sh

```

*Press `Ctrl+C` to stop the decoder. The script will automatically unload the kernel module.*

## Manual Build & Usage

If you prefer running commands manually:

1. **Compile:** `make`
2. **Load:** `sudo insmod shadow.ko`
3. **Run Decoder:** `python3 decoder.py`
4. **Unload:** `sudo rmmod shadow`

## Project Structure

* `shadow.c`: The kernel module source code.
* `decoder.py`: User-space Python script for log parsing.
* `Makefile`: Build configuration for kernel headers.
* `run.sh`: Automated build and execution script.

## License

This project is licensed under the GNU General Public License v2.0 (GPL-2.0). See the `LICENSE` file for details.
