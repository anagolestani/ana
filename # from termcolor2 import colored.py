from termcolor2 import colored
import os
import random
import time
from tqdm import tqdm
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>color>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class color:
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    BLACK = '\033[30m'
    YELLOW = '\033[92m'
    WHITE = '\033[0m'
    BLOBERI = '\033[96m'
    FONT_KHATI_ZIR = '\033[4m'
    FONT_KHATI_RO = '\033[9m'
    FONT_SHIK = '\033[3m'
    ORANG = '\033[93m'
    PUR_PLE = '\033[95m'
# >>>>>>>>>>>>>>>>>>>>cls>>>>>>>>>>>>>>>>>>>>>>>
def cls():
    os.system("cls")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>password1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def password_1():
    cls()
    v = int(input(color.PUR_PLE+"enter your length password: "))
    sec = "abcdefghijklmnopqrstuvwxyz"
    pas =""
    for i in range(0, v):
        pas += random.choice(sec)
    for _ in tqdm(range(100), desc='....', ncols=75, ascii=not True, colour='magenta'):
        time.sleep(0.01)
    cls()    
    sav=int(input(f"1:see\n>>"))
    if sav == 1:
            cls()
            for _ in tqdm(range(100), desc='....', ncols=75, ascii=not True, colour='red'):
                time.sleep(0.01)
            cls()
            print(f"\npassword :{pas}\n") 
            dobar_pas=int(input(color.WHITE+"1:do you want craet again\n2:save\n3:exit\n>>"))
            if dobar_pas == 1:
               cls()
               password_1()
            elif dobar_pas  == 2:
                cls()
                num=input("file name: ") 
                f=open(f"{num}","a") 
                f.write(f"{pas}\n")   
                f.close()
                cls()
                for _ in tqdm(range(100), desc='....', ncols=75, ascii=not True, colour='red'):
                    time.sleep(0.01)
                cls()
                print(color.PUR_PLE+"your password is saved:)")
            else :
               exit()
# .>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>password2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def password_2():
    cls()
    v = int(input(color.PUR_PLE+"enter your length password: "))
    sec = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pas =""
    for i in range(0, v):
        pas += random.choice(sec)
    for _ in tqdm(range(100), desc='....', ncols=75, ascii=not True, colour='magenta'):
        time.sleep(0.01)
    cls()    
    sav=int(input(f"1:see\n>>"))
    if sav == 1:
            cls()        
            for _ in tqdm(range(100), desc='....', ncols=75, ascii=not True, colour='red'):
                time.sleep(0.01)
            cls()    
            print(f"\npassword :{pas}\n") 
            dobar_pas=int(input(color.WHITE+"1:do you want craet again\n2:save\n3:exit\n>>"))
            if dobar_pas == 1:
               cls()
               password_2()
            elif dobar_pas  == 2:
                cls()
                num=input("file name : ") 
                f=open(f"{num}","a") 
                f.write(f"{pas}\n")   
                f.close()
                cls()
                for _ in tqdm(range(100), desc='....', ncols=75, ascii=not True, colour='red'):
                    time.sleep(0.01)
                cls()    
                print(color.PUR_PLE+"your password is saved:)")
            else :
               exit()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>password3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def password_3():
    cls()
    v = int(input(color.PUR_PLE+"enter your length password: "))
    sec ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ432123156376753890-0--0347857266001244156235"
    pas =""
    for i in range(0, v):
        pas += random.choice(sec)
    for _ in tqdm(range(100), desc='....', ncols=75, ascii=not True, colour='magenta'):
        time.sleep(0.01)
    cls()    
    sav=int(input(f"1:see\n>>"))
    if sav == 1:
            cls()
            for _ in tqdm(range(100), desc='....', ncols=75, ascii=not True, colour='red'):
                time.sleep(0.01)
            cls()    
            print(f"\npassword :{pas}\n") 
            dobar_pas=int(input(color.WHITE+"1:do you want craet again\n2:save\n3:exit\n>>"))
            if dobar_pas == 1:
               cls()
               password_3()
            elif dobar_pas  == 2:
                cls()
                num=input("file name: ") 
                f=open(f"{num}","a") 
                f.write(f"{pas}\n")   
                f.close()
                cls()
                for _ in tqdm(range(100), desc='....', ncols=75, ascii=not True, colour='red'):
                    time.sleep(0.01)
                cls()    
                print(color.PUR_PLE+"your password is saved :)")
            else :
               exit()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ejra>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def run_function():
    cls()
    option = int(input(color.FONT_SHIK+""" 
    1:easy \n
    2:medum\n
    3:difficult\n            >>> """))
    if option == 1 :
        cls()
        password_1()
    elif option == 2:
        cls()
        password_2()
    else:
        cls()
        password_3()
    point1=["5%","6%","7%","8%","9%","10%"]
    point2=["10%","20%","30%","50%","25%","35%","40%","45%"]
    point3=["50%","60%","70%","80%","90%","100%","55%","65%","75%"]
    rand1=random.sample(point1,1)  
    rand2=random.sample(point2,1)  
    rand3=random.sample(point3,1)  
    point_pas=input(color.WHITE+"do you want  to see your password point[y/n]:\n")
    if point_pas == "y":
        if apitn == 1:
            print(color.PUR_PLE+f"your password point  5% to 10% :\t{rand1}")  
        elif apitn == 2:
            print(color.PUR_PLE+f"your password point  10% to 50% :\t{rand2}") 
        elif apitn == 3:
            print(color.BLOBERI+f"your password point  50% to 100% :\t{rand3}") 
    else:
        print(color.RED+f"by")        
run_function()