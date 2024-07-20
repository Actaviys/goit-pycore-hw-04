




#-------------------------------------------------------------------
# path = 'task_2/cats_list.txt'


# def get_cats_info(path):
#     list_res = [] #Порожній список для словників
    
#     try: #Перевіряю чи правильно вказано ім'я до файла
#         file = open(file=path, mode='r', encoding='utf-8') #Відкриваю: файл, задаю мод, кодування'utf-8'
#         read_f = file.read() #Читаю файл
#     except:
#         return ("Перевірте ім'я файла і папки")
    
#     read_st = read_f.strip("\n") #Видаляю зайві рядки на початку і кінці
#     read_s = read_st.split("\n") #Розбиваю в список по переносу рядка
 
#     try: #Перевіряю щоб не було порожніх рядків
#         for i in read_s:
#             list = {} #Створюю порожній словник
#             s = i.split(",") #Розбиваю на список
#             list["id"] = s[0] #Добавляю id по індексу зі списку
#             list["name"] = s[1] #Добавляю name по індексу зі списку
#             list["age"] = s[2] #Добавляю age по індексу зі списку
#             list_res.append(list) #Записую все з словника в список
#         return list_res #Виводжу результат
#     except:
#         return ("Видаліть порожні рядки між рядками у файлі")

    
# result = get_cats_info(path)
# print(result)




#-------------------------------------#
# path = 'task_1@/txt_wage.txt' #Шлях до папки з файлом

# def total_salary(path):
#     try: #Вирішив загорнути весь код в try
#         file = open(file=path, mode='r+', encoding='utf-8') #Відкриваю: файл, задаю мод, кодування'utf-8'
#         read_f = file.read() #Читаю файл
#         read_st = read_f.strip("\n") #Видаляю зайві рядки на початку і кінці
#         read_s = read_st.split("\n") #Розбиваю по переносу рядка
        
#         counter = int(0) #Змінна лічильника
#         sum = 0 #Змінна int для додавання
#         for s in read_s:
#             counter = counter + 1 #Плюсую до лічильника
            
#             d_s = s.split(",") #Розбиваю на список
#             r_s = int(d_s[1]) #Витягую ЗП зі списку по індексу і переводжу в int
            
#             sum = r_s + sum #Додаю до змінної з попереднім результатом ЗП і зберігаю загальну суму    
#             aver = sum / counter #Вираховую середнє значення
            
#         file.close() #Закрити файл
#         return f"Загальна сума: {sum} \nСереднє значення: {aver}"
    
#     except: #Помилка
#         return "файл відсутній або пошкоджений"
        


# #Виводжу результат функції
# res = total_salary(path)
# print(res)




##################################
# import os

# dir = 'draft_folder' #Назва папки
# file = 'txt_test.txt' #Назва файлу
# path = os.path.join(dir,file) #Об'єдную папку і файл




# def total_salary(path):
#     file = open(file=path, mode='r+', encoding='utf-8') #Відкриваю: файл, задаю мод, кодування'utf-8'
#     read_f = file.read() #Читаю файл
#     read_st = read_f.strip("\n") #Видаляю зайві рядки на початку і кінці
#     read_s = read_st.split("\n") #Розбиваю по переносу рядка
    
#     file.close() #Закрити файл
    
#     counter = int(0)
#     r_p = int(0) #Змінна int для додавання
#     for s in read_s:
#         counter = counter + 1
#         d_s = s.split(",") #Розбиваю на список
#         r_s = int(d_s[1]) #Витягую ЗП зі списку по індексу і переводжу в int
        
#     sum = r_p + r_s #Додаю до змінної з попереднім результатом ЗП і зберігаю загальну суму    
#     aver = sum / counter #Вираховую середнє значення
        
#     return f"Загальна сума: {sum} \nСереднє значення: {aver}"
    
    
# res = total_salary(path)
# print(res)






# ##########################
# import os

# dir = 'draft_folder'
# file = 'txt_test.txt'
# path = os.path.join(dir,file)


# def total_salary(path):
#     try:
#         file = open(file=path, mode='r+', encoding='utf-8')
#         read_f = file.read()
#         print(read_f)
        
#     except:
#         print("no file")
    
    
    
#     # total_amount = "My"
#     # average_salary = "Text"
    
#     # salary = {
#     # (0,0): total_amount,
#     # (0,1): average_salary
#     # }

#     # print(read_f)
    
#     file.close()

# total_salary(path)




##########################
# import os

# dir = 'task_1'
# file = 'txt_test.txt'
# path = os.path.join(dir,file)


# def total_salary(path):

#     file = open(file=path, mode='r+', encoding='utf-8')
#     read_f = file.readlines()
#     # read_f = read_f.strip(" ")
#     # read_f = read_f.split(",")
    
#     # for i in read_f:
#     #     s = i.split("\n")
#     #     print(s)
    
#     # for i in read_f: 
#     #     t = i.strip(",")
#     #     p = read_f.split("\n")
#     #     print(p)
 
#     # r_s = read_file.strip(",")
    
    
#     # total_amount = "My"
#     # average_salary = "Text"
    
#     # salary = {
#     # (0,0): total_amount,
#     # (0,1): average_salary
#     # }
#     file.close()
#     print(read_f)
#     return read_f

# res = total_salary(path)
# print(res)


#-----------------------------------------------------#

# import os

# dir = 'Folder'
# file = 'txt_test.txt'
# path = os.path.join(dir,file)

# ##Створити папку з вкладеним файлом
# if not os.path.exists(path):
#     os.mkdir("Folder")
#     file = open(file=path, mode='w', encoding='utf-8')
#     file.write("First line")
#     file.close()

# #Прочитати файл
#  #
# # ##Option(1) try\except
# # try:
# #     file = open(file=path, mode='r', encoding='utf-8')
# #     print(file.read())
# #     file.close()
# # except:
# #     print("no file")
#  #
# # ##Option(2)
# # if os.path.exists(path):
# #     file = open(file=path, mode='r', encoding='utf-8')
# #     print(file.read())
# #     file.close()
# # else:
# #     print(None)
    
    
##  
# try:
#     file = open(file=path, mode='r', encoding='utf-8')
#     # red_txt = file.read()
#     print(file.read())
#     file.close()
# except:
#     print("no file")
######################################    
    
    
    
    
# b = 3
# def rec_sum(n: int) -> int: #5-> 5+4..+1
#     #Зупинка рекурсії
#     if n <= 0:
#         return 0
    
    
#     #Виклик рекурсії
#     return n + rec_sum(n-1)

# print(rec_sum(b))



# def rec_sum(n: int, level: int = 0) -> int:
#     if n <= 0:
#         print(f"rec_sum({n}): 0")
    
#     print()
#     result = n + rec_sum(n - 1, level=level + 1)
    
#     return result
    
    
    
    
    
    
    
    
    
    