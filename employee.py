from syndicate import Syndicate
from utils import check_type_of_worker_payment, find_worker

employees = []

class Employee:

    def __init__(self, name, address, type_of_worker, type_of_payment, syndicate, Id):
        self.name = name
        self.address = address
        self.type_of_worker = check_type_of_worker_payment(type_of_worker)
        self.type_of_payment = type_of_payment
        if syndicate:
            self.syndicate = Syndicate()
        else:
            self.syndicate = "Funcionário não faz parte de nenehum sindicato."
        self.Id = Id
        print("Foi adicionado o seguinte funcionário: ")
        self.print_data()

    def remove_employee(reference):
        to_remove = find_worker(reference, employees)

        if to_remove == None:
            print("Esse funcionário não existe")
        else:
            print(f"O funcionário {to_remove.name} com Id = {to_remove.Id} foi removido.")
            employees.remove(to_remove)

    def print_data(self):
        print(f"O nome do empregrado é {self.name} \nMora no endereço {self.address} \nÉ do tipo {self.type_of_worker} \nID = {self.Id}")

