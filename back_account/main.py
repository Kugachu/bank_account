from class_account import BankAccount
from functions import start_session, display_board, get_name, clients_dict, set_operation, write_account_info

CREATE = 1
SHOW = 2
EARN = 3
WITHDRAWAL = 4
QUIT = 5

clients = {}

if start_session():
    while True:
        display_board()
        choice = set_operation()

        if choice == CREATE:
            name = get_name()
            client = BankAccount(name)
            clients_dict(clients, client.id, client.name, client.balance)
            print(client.get_id(), '\t', client.get_name(), '\t', client.get_balance())
            write_account_info(client.id, client.name, client.balance)

        if choice == SHOW:
            id_number = int(input('Введите ID клиента: '))
            while id_number not in clients:
                print('ID клиента не найден')
                id_number = int(input('Введите ID клиента еще раз: '))
            print(clients[id_number])

        if choice == EARN:
            id_number = int(input('Введите ID клиента: '))
            while id_number not in clients:
                print('ID клиента не найден')
                id_number = int(input('Введите ID клиента еще раз: '))
            name = input('Введите имя клиента')
            while name not in clients[id_number]:
                print('Имя клиента не найдено')
                name = input('Введите имя клиента еще раз: ')

            new_balance = float(input('Введите сумму пополнения: '))
            clients[id_number][name] += new_balance
            print('Баланс пополнен')

        if choice == WITHDRAWAL:
            id_number = int(input('Введите ID клиента: '))
            while id_number not in clients:
                print('ID клиента не найден')
                id_number = int(input('Введите ID клиента еще раз: '))
            name = input('Введите имя клиента')
            while name not in clients[id_number]:
                print('Имя клиента не найдено')
                name = input('Введите имя клиента еще раз: ')

            new_balance = float(input('Введите сумму снятия: '))
            if clients[id_number][name] < 0 or clients[id_number][name] < new_balance:
                print('Недостаточно средств на балансе')
            clients[id_number][name] -= new_balance
            print('Средства сняты с баланса')

        if choice == QUIT:
            print('Хорошего дня.')
            break

print(clients)