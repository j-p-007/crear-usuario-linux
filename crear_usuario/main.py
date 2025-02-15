import subprocess
import pwd
import os

USER_NAME = "hacker"
PASSWORD = "SuperSecurePass123!"
LOG_FILE = "/tmp/user_creation.log"

def log_message(message):
    """Escribe logs en un archivo"""
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")

def user_exists(username):
    """ Verifica si el usuario ya existe en el sistema """
    try:
        pwd.getpwnam(username)
        return True
    except KeyError:
        return False

def create_user():
    """ Crea un usuario y guarda logs """
    log_message("🔍 Iniciando creación de usuario...")

    if user_exists(USER_NAME):
        log_message(f"⚠️ El usuario '{USER_NAME}' ya existe. No se realizará ninguna acción.")
        return

    try:
        log_message(f"✅ Creando usuario: {USER_NAME}")

        # Crear usuario con home y shell bash
        result = subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash", USER_NAME],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        log_message(f"Salida useradd: {result.stdout}")
        log_message(f"Error useradd: {result.stderr}")

        # Establecer la contraseña
        result = subprocess.run(["sudo", "bash", "-c", f"echo '{USER_NAME}:{PASSWORD}' | chpasswd"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        log_message(f"Salida chpasswd: {result.stdout}")
        log_message(f"Error chpasswd: {result.stderr}")

        # Agregar usuario al grupo sudo (opcional)
        result = subprocess.run(["sudo", "usermod", "-aG", "sudo", USER_NAME],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        log_message(f"Salida usermod: {result.stdout}")
        log_message(f"Error usermod: {result.stderr}")

        log_message("✅ Usuario creado exitosamente.")

    except subprocess.CalledProcessError as e:
        log_message(f"❌ Error al crear el usuario: {str(e)}")

if __name__ == "__main__":
    create_user()
