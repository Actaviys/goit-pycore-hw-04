
import os


#  task_3\Files
# console = input("Введіть шлях до директорії \n==>")
console = "task_3"


def console_decode(console):
    list_d = os.listdir(console)#Повертаю список файлів в папці
    # string_l = '!'.join(list_d)#Збиваю до купи список
    
    for l in list_d:
        print(f"\t{l}")    
    
        

res = console_decode(console)
print(res)
