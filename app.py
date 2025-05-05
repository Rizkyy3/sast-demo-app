import subprocess

def greet(name):
    print(f"Hello, {name}!")

def run_command(cmd):
    # WARNING: Kerentanan command injection
    # Bandit akan mendeteksi baris ini karena penggunaan shell=True
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    name = input("Enter your name: ")
    greet(name)

    cmd = input("Enter a command to run: ")
    run_command(cmd)
import subprocess

def greet(name):
    print(f"Hello, {name}!")

def run_command(cmd):
<<<<<<< HEAD
    subprocess.call(cmd, shell=True)  # VULNERABILITY: command injection
=======
    subprocess.call(cmd, shell=True)
>>>>>>> 342612c (Initial commit with vulnerable application)

if __name__ == "__main__":
    name = input("Enter your name: ")
    greet(name)

    cmd = input("Enter a command to run: ")
    run_command(cmd)
<<<<<<< HEAD
=======

>>>>>>> 342612c (Initial commit with vulnerable application)
