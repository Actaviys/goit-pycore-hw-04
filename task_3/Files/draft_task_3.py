
import os


# task_3/Files
console = input("Введіть шлях до директорії \n==>")

def console_decode(console):
    list_d = f"{os.listdir(console)}"#Повертаю список файлів в папці
    
    return list_d


res = console_decode(console)
print(res)
