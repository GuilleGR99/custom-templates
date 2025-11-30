import os
import subprocess
import shutil

init_git = "{{ cookiecutter.init_git }}".lower()

def run(cmd):
    subprocess.run(cmd, check=False)

# Si git está instalado, inicializa repo
if init_git == "yes" and shutil.which("git"):
    run(["git", "init"])
    run(["git", "add", "."])
    run(["git", "commit", "-m", "Initial commit"])