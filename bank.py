from datetime import datetime
from prettytable import PrettyTable


class Bank:
    def __init__(self):
        self.accounts = dict()
        self.operations = list()

    def deposit(self, client: str, amount: int, description: str):
        """Операция пополнения счета на сумму"""
        try:
            self.accounts[client] += amount
        except KeyError:
            self.accounts[client] = amount
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.operations.append([description, date, amount, self.accounts[client], client])
        return "Deposit operation was successful!"

    def withdraw(self, client: str, amount: int, description: str):
        """Операция снятия со счета"""
        try:
            if self.accounts[client] >= amount:
                self.accounts[client] -= amount
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.operations.append([description, date, -amount, self.accounts[client], client])
                return "Withdrawal operation was successful!"
            else:
                return "Not enough money"
        except KeyError:
            return "Client not found"

    def show_bank_statement(self, client: str, since: str, till: str):
        """Показывает выписку из банка"""
        timing = []
        for i in self.operations:
            if since <= i[1] <= till and i[4] == client:
                timing.append(i)
        if not timing:
            return "No operations during that period or client not found"
        return self.create_table(timing)

    def create_table(self, timing: list):
        """Создание таблицы"""
        table = PrettyTable()
        table.field_names = ["Date", "Description", "Withdrawals", "Deposits", "Balance"]
        w, d = 0, 0
        table.add_row(["", "Previous balance", "", "", f"${d:.2f}"])
        table.add_row(["-------------------", "----------------", "-----------", "--------", "-------"])
        for i in timing:
            if i[2] > 0:
                table.add_row([i[1], i[0], "", f"${abs(i[2]):.2f}", f"${abs(i[3]):.2f}"])
                d += i[2]
            if i[2] < 0:
                table.add_row([i[1], i[0], f"${abs(i[2]):.2f}", "", f"${abs(i[3]):.2f}"])
                w += i[2]
        table.add_row(["-------------------", "----------------", "-----------", "--------", "-------"])
        table.add_row(["", "Total", f"${abs(w):.2f}", f"${abs(d):.2f}", f"${self.accounts[client]:.2f}"])
        return table


if __name__ == "__main__":
    print('Service started! Enter "exit" to close service')
    a = Bank()
    while True:
        mess_in = input()
        if mess_in == "exit":
            print("Goodbye")
            break
        else:
            mess = mess_in.split("--")
            try:
                command = mess[0]
                client = mess[1].split('"')[1]
                description = mess[3].split('"')[1]
            except IndexError:
                print("Wrong command")
                continue
            if command == "deposit ":
                amount = mess[2].split("=")[1]
                print(Bank.deposit(a, client, int(amount), description))
            elif command == "withdraw ":
                amount = mess[2].split("=")[1]
                print(Bank.withdraw(a, client, int(amount), description))
            elif command == "show_bank_statement ":
                amount = mess[2].split('"')[1]
                print(Bank.show_bank_statement(a, client, amount, description))
            else:
                print("Command not found", command)
