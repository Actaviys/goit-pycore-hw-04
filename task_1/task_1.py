
import os

dir = 'task_1'
file = 'txt_test.txt'
path = os.path.join(dir,file)


def total_salary(path):
    try:
        file = open(file=path, mode='r', encoding='utf-8')
        # print()
    except:
        print("no file")
        
    
     
    # total_amount = "My"
    # average_salary = "Text"
    
    # salary = {
    # (0,0): total_amount,
    # (0,1): average_salary
    # }

    print(file.read())
    
    file.close()

total_salary(path)



# print()



