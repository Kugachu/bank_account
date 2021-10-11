def start_session() -> bool:
    """Запустить терминал."""
    status = input('Запустить терминал? y/n: ')
    if status == 'y':
        status = True
    if status == 'n':
        status = False
    return status


def display_board() -> None:
    """Терминал с информацией."""
    print('Добро пожаловать!')
    print('Выберете цифру для проведения операции')

    print('1 -> стать клиентом банка')
    print('2 -> вывести баланс')
    print('3 -> пополнить баланс')
    print('4 -> снять с баланса')
    print('5 -> завершить сеанс')


def set_operation() -> int:
    """Выбрать операцию."""
    choice = int(input('Операция: '))
    return choice


def clients_dict(clients: dict, id: int, name: str, balance: float) -> dict:
    """Словарь клиентов"""
    clients[id] = {name: balance}
    return clients


def write_account_info(id: int, name: str, balance: float) -> None:
    filename = 'accounts.txt'
    with open(filename, 'a') as f:
        f.write(str(id))
        f.write(name)
        f.write(str(balance))


def read_account_info(id: int, name: str, balance: float) -> None:
    filename = 'accounts.txt'
    with open(filename) as f:
        f.readlines()


def get_name() -> str:
    """Запрашивает и возвращает имя клиента."""
    name = input('Введите имя: ')
    print(f'Имя: {name} введено.')
    return name