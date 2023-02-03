import os
import sys
import time

os.system("clear")
print("""\033[93m.
  /$$$$$$            /$$ /$$   /$$ /$$   /$$    
 /$$__  $$          | $$| $$  /$$/|__/  | $$    
| $$  \__/  /$$$$$$ | $$| $$ /$$/  /$$ /$$$$$$  
|  $$$$$$  /$$__  $$| $$| $$$$$/  | $$|_  $$_/  
 \____  $$| $$  \ $$| $$| $$  $$  | $$  | $$    
 /$$  \ $$| $$  | $$| $$| $$\  $$ | $$  | $$ /$$
|  $$$$$$/|  $$$$$$$| $$| $$ \  $$| $$  |  $$$$/
 \______/  \____  $$|__/|__/  \__/|__/   \___/  
                | $$                            
                | $$                            
                |__/                            
=====================
| [*] Name : RedSec
| [*] Team : Msec
| [*] Youtube : RED SEC
=====================

Type " start " To Strat Tools 
""")

# Bagian Menu :)

pilihan = input("SqlKit > ")

if pilihan == "start":
        os.system("python module/m1.py")
