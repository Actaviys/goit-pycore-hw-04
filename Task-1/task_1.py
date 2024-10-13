import re

"""
Функція для читання файлу з іменами і зарплатами:
Обраховує загальну і середну суму зарплат та повертає кортеж чисел
"""
def total_salary(path):
    
    def salary(salary): #Функція для обрахунку чисел в списку (приймає список) 
        ress = 0
        count = 0
        try:
            for s in salary: #Пробігаюсь циклом по списку
                ress += s #Додаю по черзі числа зі списку
                count += 1 #Рахую кількість чисел в списку 
            return (ress, int(ress/count)) #Вертаю загальну суму та середню кортежем 
        
        except: return f"Файл порожній або пошкоджений 🤷‍♂️" #Вертаю помилку про те що файл порожній
    
    
    try:
        with open(path, 'r', encoding='utf-8') as f: #Відкриваю файл для читання
            salary_list = [] #Список для зарплат
            read_f = f.readlines() #Читаю файл і зберігаю як список
            patt = r"\b[0-9]+\b" #Патерн для пошуку
            
            for read in read_f: #Цикл для читання списку
                text = read.strip('\n') #Обрізаю `\n` з тексту
                extract_num = re.search(patt, text).group() #Витягую зарплати
                salary_list.append(int(extract_num)) #Добавляю зарплати до списку
            return salary(salary_list) #Вертаю функцію яка рахує суми
    
    except: return f"Файл відсутній \nПеревірте посилання на файл \n- {path} -"    




link_file = input("Введіть посилання на файл \n-> ")
# link_file = "Task-1/txt_file.txt" #Посилання на файл
print(total_salary(link_file)) #Виводжу результат функції `total_salary()`


