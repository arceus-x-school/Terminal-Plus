import os
import shlex
import subprocess
#by @frogs_on_shoes
for clear in range(100): print()
username = os.getenv("USERNAME") or os.getenv("USER")
print("Host Checked")
while True:
    try:
        IFont = '\033[36m'
        UFont = '\033[38;5;21m'
        PFont = '\033[38;5;255m'
        print(f"{IFont}┌──({UFont}" + username + f"㉿kali{IFont})-[{PFont}~{IFont}]")
        command = input(f"└─{UFont}$ {PFont}")
        command_args = shlex.split(command)
        print()  
        subprocess.run(command_args)
        print()
        if command.strip().lower() == 'exit':
            break 
        if not command.strip():
            continue
    except FileNotFoundError:
        print(f"Command not found: {command}")
    except Exception as e:
        print(f"An error occurred: {e}")
