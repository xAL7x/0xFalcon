from os import system
pip=['optparse','requests','sys','socket','pillow','pyinstaller','subprocess','threading']
for install in pip:
    system(f'pip install {install}')