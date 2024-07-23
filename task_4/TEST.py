'''
Команди:
        @1 - "hello" - Привітання з користувачем
        @2 - "add [ім'я] [номер телефону]" - Для додавання в словник {"ім'я": "номер телефону"}
        3 - "change [ім'я] [новий номер телефону]" - Зберігає в пам'яті новий номер телефону 'phone' для контакту 'username', що вже існує в записнику.
        @4 - "phone [ім'я]" - Виводить номер телефону по імені
        @5 - "all" - Виводить всі контакти з номерами телефонів
        @6 - "exit" - закрити програму 
'''

contacts = {
        'Diana': '28456239759',
        'Lyda': '59349953',
        'Dima': '34489302048'
    }

# def change_contacts(args, contacts):
#     name, phone = args
#     print(name)

def change_cont(args, contacts):
    name = args
    phone = str(contacts)
    phone = ''.join(args) #'+'.join(['1', '2', '3'])
    for p in contacts:
        pp = str(p)
        if pp == phone:
            # contacts[pp] += 
            return contacts[pp]
    
    
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact added.\n{name}: {contacts[name]}"


# def add_contact(args, contacts):
#     name, phone = args
#     contacts[name] = phone
#     return f"Contact added.\n{name}: {contacts[name]}"
    
    
    
# names = input("==> ")
# print(change_cont(names, contacts))



# def out_contacts(contacts):
#     s_tr = ""
#     for k in contacts:
#         s_tr = f"{s_tr + k + ': ' + contacts[k]}\n"
#     return s_tr
