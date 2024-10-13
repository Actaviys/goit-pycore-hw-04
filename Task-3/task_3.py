from colorama import Style, Fore, Back
from pathlib import Path
import re

S_RESET = Style.RESET_ALL #Зберігаю в коротшу назву метод скидання стилів colorama
def read_folder(path): #Функція для читання папок
    try: 
        for read in path.iterdir(): #Проходжусь циклом по папках
            str_read = str(read) #Зберігаю шлях до папки як рядок
            
            if read.is_file(): #Якщо файл то виводжу результат читання
                list_file = re.split(r"[\\]+", str_read) #Розбиваю на список прочитаний шлях до файла
                formula_f = " " * (len(str_read) - len(list_file[-1])) #Формула для рахування відступів
                print(Fore.CYAN + formula_f, f"{list_file[-1]}" + S_RESET ) #Виводжу форматований рядок з формулою і ефектами colorama
            
            elif read.is_dir(): #
                str_dir = re.split(r"[\\]+", str_read) #Розбиваю на список прочитаний шлях до папки
                formula_d = "-" * (len(str_read) - len(str_dir[-1])) #Формула для рахування рисок
                print(Fore.YELLOW + formula_d, f"{str_dir[-1]}/" + S_RESET) #Виводжу форматований рядок з формулою і ефектами colorama
                read_folder(read) #Викликаю рекурсію
                
    except: print(Fore.RED + f"Папка відсутня або невірний шлях до папки 😢 \nПеревірте посилання - {path}" + S_RESET) #Виводжу помилку 
    
    
print("Шлях до тестової папки-> ", Fore.MAGENTA + "Task-3/Test_Folder" + S_RESET)
path_dir = input("Ведіть шлях до папки \n--> ") #Просить ввести шлях до папки

read_folder(Path(path_dir)) # Викликаю функцію читання папок