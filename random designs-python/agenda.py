agenda = {
    'pedro': {
        'cell_phone': '9512-7345',
        'email': 'pedro@gmail.com',
        'address': 'Rua paiva',
    },
    'maria': {
        'cell_phone': '9456-5710',
        'email': 'maria@gmail.com',
        'address': 'rua carlos mirante',
    },
}


def read_the_full_list():
    for name in agenda:
        search_for_a_contact(name)


def search_for_a_contact(name):
    print('-'*20)
    print(f'Name: {name}')
    for date in agenda[name]:
            print(f'{date}: {agenda[name][date]}')
    print('-'*20)


def add_or_edit_contact(name, cell, email,address):
    agenda[name] = {
        'cell_phone': cell,
        'email': email,
        'address': address,
    }
    print(f'\n[{name}],contact successfully added/edited\n')


def delete_contact(name):
    agenda.pop(name)
    print(f'\nContato "{name}" excluido com sucesso!\n')


def menu():
    print('-'*20)
    print('''Options:
    [1]-See the complete list.
    [2]-Search for a contact.
    [3]-Add contact.
    [4]-Edit contact.
    [5]-Delet contact.
    [0]-Finished program.''')
    print('-'*20)

while True:
    menu()
    option = input('Choose an option: ')

    #Read full list
    if(option == '1'):
        read_the_full_list()

    #Search contact
    elif(option == '2'):
        name = input('What is the name: ')
        try:
            search_for_a_contact(name)
        except:
            print('User not found!')

    #Add contact
    elif(option == '3' or option == '4'):
        name = input('What is the name: ')
        cell = input('Cell phone: ')
        email = input('Email: ')
        address = input('Address: ')
        add_or_edit_contact(name, cell, email,address)

    #Edit contact
    elif(option == '4'):
        pass

    #Delet contact
    elif(option == '5'):
        name = input('Which contact you want to delete?:')
        delete_contact(name)

    #Finish
    elif(option == '0'):
        print('Finished program.')
        break

    #Error
    else:
        print('Invalid option, please try again!')
