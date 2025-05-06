import subprocess
import shlex

def greet(name):
    print(f"Hello, {name}!")

def run_command(cmd):
    # Memastikan bahwa cmd dipecah dengan aman dan tanpa shell=True
    args = shlex.split(cmd)
    subprocess.call(args)

if __name__ == "__main__":
    name = input("Enter your name: ")
    greet(name)

    cmd = input("Enter a command to run: ")
    run_command(cmd)
