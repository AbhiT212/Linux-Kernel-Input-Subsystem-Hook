#!/bin/bash


MODULE_NAME="shadow"


echo "[-] Compiling Kernel Module..."
make > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "[!] Compilation Failed!"
    exit 1
fi

echo "[-] Inserting Module into Kernel..."
if lsmod | grep "$MODULE_NAME" &> /dev/null ; then
    echo "[!] Module already loaded. Reloading..."
    sudo rmmod $MODULE_NAME
fi

sudo insmod $MODULE_NAME.ko
if [ $? -ne 0 ]; then
    echo "[!] Failed to insert module!"
    exit 1
fi


echo "[-] Running Decoder (Press Ctrl+C to stop)..."
# We use a 'trap' to catch Ctrl+C and clean up automatically
trap "echo -e '\n[!] Stopping...'; sudo rmmod $MODULE_NAME; echo '[-] Module Unloaded.'; exit" SIGINT

python3 decoder.py


sudo rmmod $MODULE_NAME
echo "[-] Module Unloaded."
