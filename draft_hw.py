
import os

dir = 'task_1'
file = 'txt_test.txt'
path = os.path.join(dir,file)

def total_salary(path):
    try:
        file = open(file=path, mode='r', encoding='utf-8')
        print(file.read())
        file.close()
    except:
        print("no file")
    
    
    # total_amount = "My"
    # average_salary = "Text"
    
    # salary = {
    # (0,0): total_amount,
    # (0,1): average_salary
    # }

    print(path)

total_salary(path)



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
    
    
    
    
    
    
    
    
    
    