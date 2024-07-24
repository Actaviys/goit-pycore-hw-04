
path = 'task_2@/cats_list.txt' #Змінна з назвою розташування файла

def get_cats_info(path):
    list_res = [] #Порожній список для словників
    
    try: #Перевіряю чи правильно вказано ім'я до файла
        file = open(file=path, mode='r', encoding='utf-8') #Відкриваю: файл, задаю мод, кодування'utf-8'
        read_f = file.read() #Читаю файл
    except:
        return ("Перевірте ім'я файла і папки")
    
    read_st = read_f.strip("\n") #Видаляю зайві рядки на початку і кінці
    read_s = read_st.split("\n") #Розбиваю в список по переносу рядка
 
    try: #Перевіряю щоб не було порожніх рядків
        for i in read_s:
            list = {} #Створюю порожній словник
            s = i.split(",") #Розбиваю на список
            list["id"] = s[0] #Добавляю id по індексу зі списку
            list["name"] = s[1] #Добавляю name по індексу зі списку
            list["age"] = s[2] #Добавляю age по індексу зі списку
            list_res.append(list) #Записую все з словника в список
        return list_res #Виводжу результат
    except:
        return ("Видаліть порожні рядки між рядками у файлі")

    
result = get_cats_info(path)
print(result)
