'''
Команди:
        @1 - "hello" - Привітання з користувачем
        2 - "add [ім'я] [номер телефону]" - Для додавання в словник {"ім'я": "номер телефону"}
        @3 - "change [ім'я] [новий номер телефону]" - Зберігає в пам'яті новий номер телефону 'phone' для контакту 'username', що вже існує в записнику.
        @4 - "phone [ім'я]" - Виводить номер телефону по імені
        @5 - "all" - Виводить всі контакти з номерами телефонів
        @6 - "exit" - закрити програму 
'''





def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# all contacts
def out_all_contacts(contacts):
    s_tr = ""
    for k in contacts:
        s_tr = f"{s_tr + k + ': ' + contacts[k]}\n"
    return s_tr


# # phone Dima
# def phone_out(args, contacts):
#     p_st = ""
#     phone = ''.join(args) #'+'.join(['1', '2', '3'])
#     for p in contacts:
#         pp = str(p)
#         if pp == phone:
#             p_st = f"{p_st + pp + ": " + contacts[pp]}"
#             return p_st



# # change Dima 2232222
# def change_contact(args, contacts):
#     name, phone = args
#     contacts[name] = phone
#     return f"Change contact.\n{name}: {contacts[name]}"    


#####
# add Lisa 34489302048
def add_contact(args):
    name, phone = args
    r = f"'{name}': '{phone}'"
    # res = {f'{name}{phone}'}
    return r
#####
    

def main():
  #Словник для контактів
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
        
        elif command == "all":
            print(out_all_contacts(contacts))
        
        # elif command == "phone":
        #     print(phone_out(args, contacts))

        # elif command == "change":
        #     print(change_contact(args, contacts))
        
        
        ###
        elif command == "add":
            add = add_contact(args)
            print(add)
            # contacts.update({add})
        ###
            
        elif command == "t":
            print("TEST")
                
            
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
