
import re
import os
from colorama import Fore, Back, Style

#  task_3@\Files
console = input(f"{Fore.MAGENTA}Введіть шлях до директорії \n==> {Style.RESET_ALL}")
# console = "task_3@"  



def console_decode(console):
    try: #Просто загнав весь код в `try` :)
        list_d = os.listdir(console)#Повертаю список файлів в папці
        print(f"\n{Back.BLUE}{console}:{Style.RESET_ALL}")

        for l in list_d:
            ls = str(l)
            low = ls.lower()
            
            s_format = re.search(r"(.\b[a-z]+\b)", low)
            if s_format == None:
                print(f"{Back.BLUE}\t{ls}:{Style.RESET_ALL}")
                ls_dir = os.listdir(f"{console}/{ls}")#Повертаю список файлів в папці
                for fs in ls_dir:
                    s_fs = re.search(r"(.\b[a-z]+\b)", fs) #Шукаю текст після крапки
                    if s_fs == None: #Якщо None то читаю вкладену папку
                        print(f"{Back.BLUE}\t\t{fs}:{Style.RESET_ALL}")
                        dir = os.listdir(f"{console}/{ls}/{fs}")#Повертаю список файлів в папці
                        for n in dir: #Читаю вкладену папку
                            print(f"{Fore.GREEN}\t\t\t{n}:{Style.RESET_ALL}")
                            
                    if s_fs != None: #Якщо немає папки то виводжу назву
                        print(f"{Fore.GREEN}\t\t{fs}{Style.RESET_ALL}")
             
                    
            if s_format != None: #Якщо немає папки то виводжу решту файлів
                print(f"{Fore.GREEN}\t{ls}{Style.RESET_ALL}") 
                
    except:#Виводжу попередження
        print(f"Перевірте ім'я директорії-> {Fore.RED}{console}{Style.RESET_ALL}")
        

  
console_decode(console) #Виклик функції
        
