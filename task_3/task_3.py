
import os


#task_3/txt_list_3.txt
console = input("Введіть шлях до директорії \n==>")

def console_decode(console):
    
    return os.listdir(console) #Повертаю список файлів в папці


res = console_decode(console)
print(res)
