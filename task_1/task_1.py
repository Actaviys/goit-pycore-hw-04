
path = 'task_1@/txt_wage.txt' #Шлях до папки з файлом

def total_salary(path):
    try: #Вирішив загорнути весь код в try
        file = open(file=path, mode='r+', encoding='utf-8') #Відкриваю: файл, задаю мод, кодування'utf-8'
        read_f = file.read() #Читаю файл
        read_st = read_f.strip("\n") #Видаляю зайві рядки на початку і кінці
        read_s = read_st.split("\n") #Розбиваю по переносу рядка
        
        counter = int(0) #Змінна мічильника
        sum = 0 #Змінна int для додавання
        for s in read_s:
            counter = counter + 1 #Плюсую до лічильника
            
            d_s = s.split(",") #Розбиваю на список
            r_s = int(d_s[1]) #Витягую ЗП зі списку по індексу і переводжу в int
            
            sum = r_s + sum #Додаю до змінної з попереднім результатом ЗП і зберігаю загальну суму    
            aver = sum / counter #Вираховую середнє значення
            
        file.close() #Закрити файл
        return f"Загальна сума: {sum} \nСереднє значення: {aver}"
    
    except: #Помилка
        return "файл відсутній або пошкоджений"
        


#Виводжу результат функції
res = total_salary(path)
print(res)
