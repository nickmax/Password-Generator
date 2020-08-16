#Imports the 'random' Builtin Module
import random
import pyperclip
from random import choice
from pyperclip import copy
import tqdm
from tqdm import *
import time
import colored
from colored import fg,bg,attr

characters = list("abcdefghijk!@#$%^&*()lmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~`_+d|\<?/>.,2-")
random= choice(characters)

red = fg("red")
green = fg('green')
blue = fg('blue')
yellow = fg('yellow')
reset = attr("reset")
cyan = fg("cyan")



def banner():
    print(red+" ____   _    ____ ______        _____  ____  ____  "+reset)
    print(green+"|  _ \ / \  / ___/ ___\ \      / / _ \|  _ \|  _ \ "+reset)
    print(blue+"| |_) / _ \ \___ \___ \\ \ /\ / / | | | |_) | | | |"+reset)
    print(green+"|  __/ ___ \ ___) |__) |\ V  V /| |_| |  _ <| |_| |"+reset)
    print(yellow+"|_| /_/   \_\____/____/  \_/\_/  \___/|_| \_\____/ "+reset)
    print()                                               
    print(yellow+"  ____ _____ _   _ _____ ____      _  _____ ___  ____   "+reset)
    print(red+" / ___| ____| \ | | ____|  _ \    / \|_   _/ _ \|  _ \  "+reset)
    print(green+"| |  _|  _| |  \| |  _| | |_) |  / _ \ | || | | | |_) | "+reset)
    print(blue+"| |_| | |___| |\  | |___|  _ <  / ___ \| || |_| |  _ <  "+reset)
    print(green+"\____|_____|_| \_|_____|_| \_\/_/   \_\_| \___/|_| \_\ "+reset)
    
    
def generate():
    
    passwordlength = int(input(cyan+"Please input Password Length >>"+reset))
    x =choice(characters)
    password = x
    for f in range(passwordlength-1):
        password += choice(characters)        
    for i in tqdm(range(100)):
            time.sleep(0.01)
    print(green +"PassWord Generated Successfully!"+reset)
    print()
    print(">>   " + password)
    pyperclip.copy(password)
    print(yellow+"PassWord copied succesfully "+reset)


banner()
generate()


            






 
