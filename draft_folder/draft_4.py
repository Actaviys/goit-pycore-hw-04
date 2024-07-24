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
def out_all_contacts(contacts):
    s_tr = ""
    for k in contacts:
        s_tr = f"{s_tr + k + ': ' + contacts[k]}\n"
    return s_tr

# phone Dima
def phone_out(args, contacts):
    p_st = ""
    phone = ''.join(args)
    for p in contacts:
        pp = str(p)
        if pp == phone:
            p_st = f"{p_st + pp + ": " + contacts[pp]}"
            return p_st


# change Dima 3333333333
def change_contact(args, contacts):
    name, phone = args
    for c in contacts:
        cc = str(c)
        if cc == name:
            c_st = f"The contact - {name} - already exists\nReplace contact (1-Yes / 0-No)?"
            conf = int(input(f"{c_st}\nenter 1 or 0 -> "))
            if conf == 1:
                contacts[name] = phone
                return "Contact changed"
            else: return "Ok"
            

# add Lisa 34489302048
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Add contact \n{name}: {contacts[name]}"
    

#Словник для контактів
contacts = { 
    'Diana': '28456239759',
    'Lyda': '59349953',
    'Dima': '34489302048'
}

#Обробляю команди
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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


if __name__ == "__main__":
    main()





# ###################################################################
# #Най простіший спосіб зчитати командний рядок
# def main():
#     print("Welcome to the assistant bot!")
#     while True:
#         command = input("Enter a command: ").strip().lower()

#         if command in ["close", "exit"]:
#             print("Good bye!")
#             break

#         elif command == "hello":
#             print("How can I help you?")
        
#         else:
#             print("Invalid command.")

# if __name__ == "__main__":
#     main()
