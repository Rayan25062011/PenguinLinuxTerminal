import time
from pystyle import Col 
from os import system, name
import os
from tqdm import tqdm, trange
from progress.bar import FillingSquaresBar
import sys
import socket
import warnings
newfile = False
root = False
print("""

██████╗░███████╗███╗░░██╗░██████╗░██╗░░░██╗██╗███╗░░██╗  ██╗░░░░░██╗███╗░░██╗██╗░░░██╗██╗░░██╗
██╔══██╗██╔════╝████╗░██║██╔════╝░██║░░░██║██║████╗░██║  ██║░░░░░██║████╗░██║██║░░░██║╚██╗██╔╝
██████╔╝█████╗░░██╔██╗██║██║░░██╗░██║░░░██║██║██╔██╗██║  ██║░░░░░██║██╔██╗██║██║░░░██║░╚███╔╝░
██╔═══╝░██╔══╝░░██║╚████║██║░░╚██╗██║░░░██║██║██║╚████║  ██║░░░░░██║██║╚████║██║░░░██║░██╔██╗░
██║░░░░░███████╗██║░╚███║╚██████╔╝╚██████╔╝██║██║░╚███║  ███████╗██║██║░╚███║╚██████╔╝██╔╝╚██╗
╚═╝░░░░░╚══════╝╚═╝░░╚══╝░╚═════╝░░╚═════╝░╚═╝╚═╝░░╚══╝  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝

""")
print(Col.red +"""
         .::::.
  __...::O:::::
,''''::::::'  ::
      `':'':..:::
       :  ::::::::
       :  ::::::::::
      :  ::::::::::
      :  ::::::::::
      :  ::::::::::
      : :::::::::::
      : :::: ::::::
      : :::: ::::::
      : ::: .::::::
      : ::: :::::::
      :  :: :::::::
       :  : ::::::'
       .:  :::::::
    ,;;::'.:::::::

""")
user = input("Enter username: ")
while True:
    termCMD = input(Col.blue +f"penguin@{user}$ ")
    if termCMD == Col.red +"clear":
        system("cls")
    if termCMD ==  "ls":
        os.system("dir")
    if termCMD == "quit":
        quit()
    if termCMD == "sudo -s":
        while True:
            sudoCMD = input(f"root@{user}$ ")
            root = True
            if sudoCMD == "pip install aircrack -ng":
                print(Col.red +"Downloading aircrack.tar.giz...")
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(0.3)
                        pbar.update(10)
            if sudoCMD == "cd Desktop":
                while True:
                    desktopCMD = input("root@kali:~/Desktop$ ")
                    if desktopCMD == "makefile":
                        filename = input("File name: ")
                        filecontent = input("File content: ")
                        print("File created!")
                        newfile = True
                    if desktopCMD == f"vim {filename}":
                        print(filecontent)
                    if desktopCMD == f"cd {filename}":
                        while True:
                            fileCMD = input(f"root@kali:~/{filename}")
                            if fileCMD == f"del {filename}":
                                print(f"You do not have permission to delete {filename}")
            if sudoCMD == "ls":
                os.system("dir")
            if sudoCMD == "passwd":
                passwd = input("New password: ")
                print("Uploading new password to secure location...")
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(0.8)
                        pbar.update(10)
                        print("Complete!")
                    passwdData = f"{passwd})
            if sudoCMD == "":
                print("Invalid command")
            if sudoCMD == "dragon":
                print(Col.red + """
         .::::.
  __...::O:::::
,''''::::::'  ::
      `':'':..:::
       :  ::::::::
      :  ::::::::::
      :  ::::::::::
      :  ::::::::::
      :  ::::::::::
      : :::::::::::
      : :::: ::::::
      : :::: ::::::
      : ::: .::::::
      : ::: :::::::
      :  :: :::::::
       :  : ::::::'
       .:  :::::::
    ,;;::'.:::::::


                """)
            if sudoCMD == "title":
                print("""
                ██████╗░███████╗███╗░░██╗░██████╗░██╗░░░██╗██╗███╗░░██╗  ██╗░░░░░██╗███╗░░██╗██╗░░░██╗██╗░░██╗
██╔══██╗██╔════╝████╗░██║██╔════╝░██║░░░██║██║████╗░██║  ██║░░░░░██║████╗░██║██║░░░██║╚██╗██╔╝
██████╔╝█████╗░░██╔██╗██║██║░░██╗░██║░░░██║██║██╔██╗██║  ██║░░░░░██║██╔██╗██║██║░░░██║░╚███╔╝░
██╔═══╝░██╔══╝░░██║╚████║██║░░╚██╗██║░░░██║██║██║╚████║  ██║░░░░░██║██║╚████║██║░░░██║░██╔██╗░
██║░░░░░███████╗██║░╚███║╚██████╔╝╚██████╔╝██║██║░╚███║  ███████╗██║██║░╚███║╚██████╔╝██╔╝╚██╗
╚═╝░░░░░╚══════╝╚═╝░░╚══╝░╚═════╝░░╚═════╝░╚═╝╚═╝░░╚══╝  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝
                """)
            if sudoCMD == "echo":
                echo = input("echo ")
                print(echo)
            if sudoCMD == "cd PenguinLinux.py":
                print("You are not the creator of Penguin Linux")
            if sudoCMD == "chmod +x PenguinLinux.py":
                print("Nice try haha.")
            if sudoCMD == "top":
                try:
                    os.system("top") 
                except KeyboardInterrupt:
                    print("KeyboardInterrupt")
            if "mkdir" in sudoCMD:
                os.system(f"{sudoCMD}")
            if "sudo" in sudoCMD:
            os.system(f"{sudoCMD}")
            if "history" in sudoCMD:
                os.system(f"{sudoCMD}")
            if "cd ~" in sudoCMD:
                os.system(f"{sudoCMD}")
            if "chmod +x" in sudoCMD:
                os.system(f"{sudoCMD}")
            if "python3 " in sudoCMD:
                os.system(f"{sudoCMD}")
            if "pip " in sudoCMD:
                os.system(f"{sudoCMD}")
            # Do everything quickly:
            try:
                os.system(sudoCMD)
            except "sudo -s" in sudoCMD:
                ignore()
            warnings.filterwarnings("ignore")
