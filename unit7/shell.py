''' Shell example. Needs subproces module to execute commands'''
import subprocess

def main():
    ''' main procedure '''
    while True:
        entry = input("$ ")
        if entry == "exit":
            break
        execute_command(entry)

def execute_command(command):
    ''' execute command '''
    try:
        # using split() to send parameters as well
        subprocess.run(command.split())
    except Exception:
        print(f"error: command {command} not found ")

main()
