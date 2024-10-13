
""" 
Функція що генерує список словників на основі текстового файлу
в якому всі значення розбиті через кому (id, name, age)
"""
def get_cats_info(path):
    return_list = [] #Порожній список для результату
    
    try: #Огортаю весь код функції в try
        with open(path, 'r', encoding='utf-8') as f: #Відкриваю файл
            read_f = f.readlines() #Читаю файл
            
            for red in read_f: #Читаю список
                line_reader = red.strip('\n').split(',') #Читаю рядки і записую в список
                
                dict_cats = {   #Створюю словник із значеннями з списка
                    "id": line_reader[0],
                    "name": line_reader[1],
                    "age": line_reader[2]
                    }
                return_list.append(dict_cats) #Записую словник в список
            return return_list #Повертаю список
        
    except: return f"Перевірте посилання на файл \n- {path} -" #Повертаю помилку якщо невірне посилання


link_file = "Task-2/txt_file_2.txt" #Посилання на файл
print(get_cats_info(link_file)) #Виводжу результат функції