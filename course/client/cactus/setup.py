import sys 
from cx_Freeze import setup,  Executable

build_exe_options = {"packages":["os","pygame","sys","random","time",
                    "requests","json","copy","pygame.font",],
                    "include_files":["arrow.py","authorization.py",
                    "button.py","clicker.py","game_stats.py",
                    "menu.py","multiplayer.py","registration.py",
                    'scoreboard.py',"settings.py","shop.py","images/",
                    "sounds/"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "Cactus evolution",
    version = "1.1",
    author = "Ablyamitov Enver",
    description = "Cactus game!",
    options = {"build_exe":build_exe_options},
    executables = [Executable("main.py",base = base)])