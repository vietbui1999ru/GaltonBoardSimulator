import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


if __name__ == '__main__':

    # get packages
    packages = ["pygame", "pymunk", "pygame_gui", "matplotlib", "numpy", "scipy"]

    for pack in packages:
        install(pack)
