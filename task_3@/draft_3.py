
import re
import os
from colorama import Fore, Back, Style

#  task_3\Files
# console = input("Введіть шлях до директорії \n==>")
console = "task_3"  



def console_decode(console):
  
    list_d = os.listdir(console)#Повертаю список файлів в папці

    print(f"{Fore.BLUE}{console}:{Style.RESET_ALL}")
    
    for l in list_d:
        ls = str(l)
        low = ls.lower()
        # r = re.search(r"[a-z]+", low)
        # print(r)
        
        s_format = re.search(r"(.\b[a-z]+\b)", low)
        if s_format == None:
            print(f"{Fore.BLUE}\t{ls}:{Style.RESET_ALL}")
            ls_dir = os.listdir(f"{console}/{ls}")#Повертаю список файлів в папці
            for fs in ls_dir:
                s_fs = re.search(r"(.\b[a-z]+\b)", fs)

                if s_fs == None:
                    print(f"{Fore.BLUE}\t\t{fs}{Style.RESET_ALL}")
                    dir = os.listdir(f"{console}/{ls}/{fs}")#Повертаю список файлів в папці
                    for n in dir:
                        print(f"{Fore.GREEN}\t\t\t{n}:{Style.RESET_ALL}")
                if s_fs != None:
                    print(f"{Fore.GREEN}\t\t{fs}{Style.RESET_ALL}a")
                       
                
                
        if s_format != None:
            print(f"{Fore.GREEN}\t{ls}{Style.RESET_ALL}") 
        # print(s_format)
        

  
console_decode(console)  
        

# res = console_decode(console)
# print("___________")
# print(res)




#####################################################
#Старт віртуалки
# .\.venv\Scripts\python.exe

# from colorama import Fore, Back, Style

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# result = f"{Back.GREEN}Dima{Style.RESET_ALL}"
# print(result)

# print('\033[31m' + 'some red text')
# print('\033[39m') # and reset to default color



##### termcolor
# from termcolor import colored
# # then use Termcolor for all colored text output
# print(colored('Hello, World!', 'green', 'on_red'))