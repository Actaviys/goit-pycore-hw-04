'''
Команди:
        @1 - "hello" - Привітання з користувачем
        @2 - "add [ім'я] [номер телефону]" - Для додавання в словник {"ім'я": "номер телефону"}
        @3 - "change [ім'я] [новий номер телефону]" - Зберігає в пам'яті новий номер телефону 'phone' для контакту 'username', що вже існує в записнику.
        @4 - "phone [ім'я]" - Виводить номер телефону по імені 
        @5 - "all" - Виводить всі контакти з номерами телефонів
        @6 - "exit" - закрити програму 
'''



# all contacts
def out_all_contacts(contacts): #Виводжу всі контакти
    s_tr = ""
    for k in contacts: #Пробігаюсь циклом і записую в змінну
        s_tr = f"{s_tr + k + ': ' + contacts[k]}\n"
    return s_tr #Повертаю змінну з рядком

# phone Dima
def phone_out(args, contacts): #Виводжу контакт по імені
    p_st = ""
    name = ''.join(args) #Перетворюю в рядок
    
    for p in contacts: #Пробігаюсь по понтактах
        pp = str(p)#Перетворюю в рядок
        if pp == name: #Шукаю збіг
            p_st = f"{p_st + pp + ": " + contacts[pp]}" #Збиваю все до купи в змінній
            return p_st #Повертаю рядок з контактом
        
    return "There is no contact"#Якщо немає


# change Dima 323423
def change_contact(args, contacts): #Якщо добавлять через 'change' то попередить про те що контакт відсутній
    name, phone = args #Розбиваю аргументи по змінних
    for c in contacts: #Пробігаюсь по контактах
        cc = str(c)
        if cc == name: #Перевіряю на співпадіння, якщо є питаю чи потрібно замінити 
            c_st = f"The contact - {name} - already exists\nReplace contact (1-Yes / 0-No)?" #Змінна з запитанням
            conf = int(input(f"{c_st}\nenter 1 or 0 -> ")) #Змінна з `input`
            if conf == 1: #Перевіряю на введене значення
                contacts[name] = phone #Якщо '1' то записую в словник
                return "Contact changed" #І вертаю повідомлення
            else: return "Ok"
            

# add Lisa 34489302048
def add_contact(args, contacts):#
    name, phone = args #Розбиваю аргументи по змінних
    contacts[name] = phone #Записую до списку
    return f"Add contact \n{name}: {contacts[name]}" #Повертаю повідомлення
    


#Словник для контактів
contacts = { 
    'Diana': '28456239759',
    'Lyda': '59349953',
    'Dima': '34489302048'
}

#Обробляю команди
def parse_input(user_input):
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
            print(out_all_contacts(contacts))
        
        elif command == "phone":
            print(phone_out(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))
        
        elif command == "add":
            add = add_contact(args, contacts)
            print(add)
                
        else:
            print("Invalid command.")



if __name__ == "__main__": #
    main()


