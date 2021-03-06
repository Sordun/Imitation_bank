# Имитация работы банка со счетами клиентов

### Требования к сервису:

- работа с сервисом должна осуществляться через _Interactive CLI_
- состояние счетов хранится только в рамках одной сессии
- у клиента может быть только один счет
- валюта у всех счетов одинаковая _USD_

### Поддерживаемые операции:

- deposit - операция пополнения счета на сумму, аргументы: client, amount, description
- withdraw - операция снятия со счета, аргументы: client, amount, description
- show_bank_statement - вывод на экран выписки со счета за период, аргументы: client, since ,till

### Пример
```bash
deposit --client="John Jones" --amount=100 --description="ATM Deposit"
```

```bash
withdraw --client="John Jones" --amount=100 --description="ATM Withdrawal"
```

```bash
show_bank_statement --client="John Jones" --since="2022-02-01 00:00:00" --till="2022-03-01 00:00:00"
```

# Установка:

1.Склонируйте к себе данный репозиторий при помощи команды:

```bash
git clone https://github.com/Sordun/Imitation_bank.git
```

2.Выполните команду для создания виртуального окружения:
```bash
python -m venv env
```

3.Активируйте созданное виртуальное окружение при помощи команды:
```bash
env\Scripts\activate
```

4.Установите необходимые пакеты в активированное окружение при помощи команды:
```bash
pip install -r requirements.txt
```

5.Для активации запустите файл:
```bash
bank.py
```
