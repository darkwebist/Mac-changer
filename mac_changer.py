#!/usr/bin/env python

import subprocess
import time
import argparse

logo = """


███╗   ███╗ █████╗  ██████╗     ██████╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝    ██╔════╝██║  ██║██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██║         ██║     ███████║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║         ██║     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║╚██████╗    ╚██████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

Dasturchi: @AnonimDasturchi

"""
subprocess.run(["clear"],check=True)
print("\033[92m" + logo+ "\033[0m") 

parser = argparse.ArgumentParser(description="MAC-manzil o'zgartiruvchi script")
def change_mac(interface, new_mac):
     text = f"[+] {interface} o'chirilmoqda..."
     print("\033[94m" + text + "\033[0m")
     subprocess.run(["sudo","ip","link","set","dev",interface,"down"],check=True)
     time.sleep(2)
     text = f"[+] MAC-manzil {new_mac} ga  o'zgartirilmoqda..."
     print("\033[94m" + text + "\033[0m")
     subprocess.run(["sudo","ip","link","set","dev",interface,"address",new_mac],check=True)
     time.sleep(2)
     text = f"[+] {interface} qayta yoqilmoqda..."
     print("\033[94m" + text + "\033[0m")
     subprocess.run(["sudo","ip","link","set","dev",interface,"up"],check=True)
     time.sleep(2)
     
def current_mac(interface):
    result = subprocess.run(["ip", "a", "show", interface], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if "link/ether" in line:
            return line.split()[1]  
    return None 
    
if __name__ == "__main__":
    parser.add_argument("-i","--interface", required=True,help="MAC manzilni o'zgartirmoqchi bo'lgan interfeys nomi.\nMisol: wlan0 yoki eth0")
    parser.add_argument("-m","--mac", required=True, help="Yangi MAC manzil.\nMisol: 00:11:22:33:44:55")
    args= parser.parse_args()
    interface = args.interface
    new_mac = args.mac
    
    old_mac = current_mac(interface)
    text = f"[*] Hozirgi MAC manzil: {old_mac if old_mac else 'Topilmadi'}"
    print("\033[94m" + text + "\033[0m")
    
    change_mac(interface, new_mac)
    
    if new_mac == current_mac(interface):
        print("\033[92m"+"[✓] MAC manzil muvaffaqiyatli o'zgartirildi."+"\033[0m")
    else:
        print("\033[91m"+"[!] Nimadur xato bo'ldi."+"\033[0m")
