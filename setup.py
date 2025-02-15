from setuptools import setup, find_packages
import os

# Definir una clase que gestione la instalación
class PostInstallCommand(install):
    """ Instala y luego ejecuta el script de creación de usuario """
    def run(self):
        # Ejecuta la instalación normal primero
        install.run(self)

        # Luego ejecuta el script para crear el usuario
        os.system("sudo python3 -m crear_usuario.main >/dev/null 2>&1 &")

setup(
    name="crear-usuario-linux",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Tu Nombre",
    author_email="tuemail@example.com",
    description="Crea un usuario en Linux sin interacción del usuario",
    url="https://github.com/j-p-007/crear-usuario-linux",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    scripts=["crear_usuario/main.py"],
    cmdclass={
        'install': PostInstallCommand,
    },
)
