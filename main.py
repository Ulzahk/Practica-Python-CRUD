import sys


clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer'
    }
]


def create_client(client):
    if client not in clients:
        clients.append(client)
    else:
        print('Client is already in the client\'s list')


def list_clients():
    print('[idx] | [name] | [company] | [email] | [position] \n')
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))
    
    print('')



def update_client(index, update_client_field):
    if index is not None:
        clients[index].update(update_client_field)
    else:
        print('Client is not in clients list')


def delete_client(index):
    if index:
        del clients[index]
    else:
        print('Client is not in client list')


def search_client(index, client_name):
    if index is not None:
        print(clients[index])
    else:
        print('There is not a client call {} in the client\'s list'.format(client_name))


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?: ')
    print('[L]ist clients')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?: '.format(field_name))
    
    return field


def _get_client_name():
    client_name = None

    while not client_name:
        client_name =  input('What is the client name?: ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _get_client_index(client_name):
    for idx, client in enumerate(clients):
        if client['name'] == client_name:
            return idx


def _set_update_field():
    updates = False
    updated_client_field = {}

    while not updates:
        field = input('What field do you want to update? [name][company][email][position]: ').lower()

        if field == 'exit':
            updates = True
            continue

        field_value = input('What is the new {}?: '.format((field)).capitalize())

        updated_client_field.setdefault(field, field_value)
        
        return updated_client_field

if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position') 
        }
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        index = _get_client_index(client_name)
        delete_client(index)
        list_clients()
    elif command == 'U':
        list_clients()
        client_name = _get_client_name()
        index = _get_client_index(client_name)
        updated_client_field = _set_update_field()
        update_client(index, updated_client_field)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        index = _get_client_index(client_name)
        found = search_client(index , client_name)
    else:
        print('Invalid command')