import subprocess
import shlex
#by tiktok @frogs_on_shoes Github @dachos
for clear in range(100): print()
while True:
    try:
        IFont = '\033[36m'
        UFont = '\033[38;5;21m'
        PFont = '\033[38;5;255m'
        print(f"{IFont}┌──({UFont}root㉿kali{IFont})-[{PFont}~{IFont}]")
        command = input(f"└─{UFont}$ {PFont}")
        command_args = shlex.split(command)
        
        subprocess.run(command_args)
        
        if command.strip().lower() == 'exit':
            break
            
        if not user_input.strip():
            continue
    except FileNotFoundError:
        print(f"Command not found: {command}")
    except Exception as e:
        print(f"An error occurred: {e}")
