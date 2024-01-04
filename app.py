import json

users = []
current_user = None

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def register_user(username, password):
    for user in users:
        if username == user['username']:
            return None
    
    new_user = {'username': username, 'password': password, 'todos': []}
    users.append(new_user)
    save_data('users.json', users)
    return new_user


def login_user(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None


def add_todo(todo, user):
    user['todos'].append(todo)
    save_data('users.json', users)


def remove_todo(index, user):
    if 1 <= index <= len(user['todos']) + 1:
        user['todos'].pop(index-1)
        save_data('users.json', users)


def show_todos(user):
    for index, todo in enumerate(user['todos'], 1):
        print(f'{index}: {todo}')


def main():
    global users, current_user
    users = load_data('users.json')

    print('\nWelcome to Todo app.\n'.center(50))
    while True:

        if not current_user:
            print('1. Register')
            print('2. Login')
            print('3. Quit')
            choice = input('Select: ')

            if choice == '1':
                username = input('Enter username: ')
                password = input('Enter password: ')
                user = register_user(username, password)

                if user:
                    print('Registration succsefully.')
                    current_user = user
                else:
                    print('Username already exist')
                    print('Please log in.')
            elif choice == '2':
                username = input('Enter username: ')
                password = input('Enter password: ')
                user = login_user(username, password)  

                if user:
                    print(f"Loged in as {user['username']}")
                    current_user = user
                else:
                    print('Please register.')  
            elif choice == '3':
                print('Bye!')
                break
            else:
                print('Invalid input. Please try again!')
                
        else:
            print(f"Loged in as {user['username']}")
            print('1. Show todos.')
            print('2. Add todo.')
            print('3. Remove todo.')
            print('4. Quit')
            choice = input('Select: ')

            if choice == '1':
                show_todos(current_user)
                save_data('users.json', users)
            elif choice == '2':
                todo = input('Enter todo: ')
                add_todo(todo, current_user)
                save_data('users.json', users)
            elif choice == '3':
                idx = int(input('Enter index of todo: '))
                remove_todo(idx, current_user)
                save_data('users.json', users)
            elif choice == '4':
                print('Bye!')
                break
            else:
                print('Invalid choice. Please try again!')


if __name__ == '__main__':
    main()