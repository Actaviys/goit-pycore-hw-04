'''
Команди:
        @1 - "hello" - Привітання з користувачем
        @2 - "add [ім'я] [номер телефону]" - Для додавання в словник {"ім'я": "номер телефону"}
        3 - "change [ім'я] [новий номер телефону]" - Зберігає в пам'яті новий номер телефону 'phone' для контакту 'username', що вже існує в записнику.
        4 - "phone [ім'я]" - Виводить номер телефону по імені 
        @5 - "all" - Виводить всі контакти з номерами телефонів
        @6 - "exit" - закрити програму 
'''


# add Lisa 34489302048
# change Rik 34482390048
# phone Dima

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact added.\n{name}: {contacts[name]}"


def out_all_contacts(contacts):
    s_tr = ""
    for k in contacts:
        s_tr = f"{s_tr + k + ': ' + contacts[k]}\n"
    return s_tr


# def change_contact(args, contacts):
#     name, phone = args
#     contacts[name] = phone
#     if contacts[name] == phone:
#         print("OK")
#     return f"{contacts}"
    
    

def main():
    contacts = {
        'Diana': '28456239759',
        'Lyda': '59349953',
        'Dima': '34489302048'
    }
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            print(add_contact(args, contacts))
        
        elif command == "all":
            print(out_all_contacts(contacts))

        # elif command == "change":
        #     print(change_contact(args, contacts))
        
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
