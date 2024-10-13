'''
Команди для консолі:
        @1 - "hello" - Привітання з користувачем
        @2 - "add [ім'я] [номер телефону]" - Для додавання в словник {"ім'я": "номер телефону"}
        @3 - "change [ім'я] [новий номер телефону]" - Зберігає в пам'яті новий номер телефону 'phone' для контакту 'username', що вже існує в записнику.
        @4 - "phone [ім'я]" - Виводить номер телефону по імені 
        @5 - "all" - Виводить всі контакти з номерами телефонів
        @6 - "exit" - закрити програму 
'''


#Словник для контактів
contacts_dict = { 
    'Dima': '1234567890',
    'Katya': '0987654321'
}

#
def add_contact(args, contacts): #Функція додавання контакту до списку
    name, phone = args #Розбиваю аргументи по змінних
    contacts[name] = phone #Записую контакт до списку
    return f"contact '{name}' added" #Повідомлення
    

#
def out_all_contacts(contacts): #Виводжу всі контакти зі словника
    result_all = ""
    for cont in contacts: #Пробігаюсь циклом по словнику
        result_all += cont + ': ' + contacts[cont] + "\n" #Записую в змінну результат читання словника
    return (result_all) #Повертаю результат


#
def contact_phone(name, contacts): #Функція пошуку номера телефону за ім'ям
    for cont in contacts: #Пробігаюсь по словнику з контактами
        if cont == name[0]: #Шукаю збіг
            return cont + ": " + contacts[cont] #Повертаю рядок з контактом і телефоном
    return "There is no contact" #Повертаю повідомлення про відсутність контакту



def change_contact(args, contacts): #Якщо добавлять через 'change' то перевірить чи контакт вже існує
    name, phone = args #Розбиваю аргументи по змінних
    for c in contacts: #Пробігаюсь по контактах
        if c == name: #Перевіряю на співпадіння
            c_st = f"The contact - {name} - already exists\nReplace contact (Yes / No)?" #Змінна з запитанням
            conf = input(f"{c_st}\nenter y or n -> ") #input з підтвердженням
            if conf == "y": #Перевіряю на введене значення
                contacts[name] = phone #Якщо '1' то записую в словник
                return "Contact changed" #Вертаю повідомлення
            
            else: return "Ok"
            




def parse_input(user_input): #Фунуція обробки команд
    cmd, *args = user_input.split() #Розбиваю по словах
    cmd = cmd.strip().lower() #Перше слово записую в окрему змінну
    return cmd, *args#Вертаю перше слово і список аргументів


def main():
    print("Welcome to the assistant bot!")
    while True: #Основний цикл для постійного запиту команд
        user_input = input("Enter a command: ") #Змінна з введеним значенням
        command, *args = parse_input(user_input) #Функціональна змінна для парсингу команд

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command == "all":
            print(out_all_contacts(contacts_dict))
        
        elif command == "add":
           print(add_contact(args, contacts_dict))
            
        elif command == "phone":
            print(contact_phone(args, contacts_dict))

        elif command == "change":
            print(change_contact(args, contacts_dict))
             
            
        else:
            print("Invalid command.")



if __name__ == "__main__": #
    main()


