from syndicate import Syndicate
from utils import check_type_of_worker_payment, find_worker

# employees = []

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

    def remove_employee(reference, employees):
        to_remove = find_worker(reference, employees)

        if to_remove == None:
            print("Esse funcionário não existe")
        else:
            print(f"O funcionário {to_remove.name} com Id = {to_remove.Id} foi removido.")
            employees.remove(to_remove)

    def edit_info(self):
        while True:
            info = input("Qual informação deseja alterar: ")
            if info.lower() == "nome":
                self.name = input("Digite o novo nome: ")
            elif info.lower() == "endereço" or info.lower() == "endereco":
                self.address = input("Digite o novo endereço: ")
            elif info.lower() == "tipo":
                self.type_of_worker = check_type_of_worker_payment(input("Digite o tipo de funcionário: "))
            elif info.lower() == "metodo de pagamento" or info.lower() == "método de pagamento":
                self.type_of_payment = input("Digite o método de pagamento desejado: ")
            elif info.lower() == "sindicato":
                temp_syndicate = input("Digite se o funcionário vai fazer parte do sindicato. [sim] [nao} :")
                if temp_syndicate.lower() == "sim" and self.syndicate == "Funcionário não faz parte de nenehum sindicato.":
                    self.syndicate = Syndicate()
                elif temp_syndicate.lower() == "nao" and temp_syndicate.lower() != "Funcionário não faz parte de nenehum sindicato.":
                    self.syndicate.delete()
                    self.syndicate = "Funcionário não faz parte de nenehum sindicato."
            elif info.lower() == "identificação no sindicato" or info.lower() == "identificacao no sindicato":
                try:
                    self.syndicate.info_edit("id")
                except:
                    print("Funcionário não faz parte de nehum sindicato")
            elif info.lower() == "taxa do sindicato":
                try:
                    self.syndicate.info_edit("taxa do sindicato")
                except:
                    print("Funcionário não faz parte de nehum sindicato")
            if input("Deseja alterar mais algum dado? [sim] [nao]\n") == "nao":
                break

    def print_data(self):
        print(f"O nome do empregrado é {self.name} \nMora no endereço {self.address} \nÉ do tipo {self.type_of_worker} \nID = {self.Id}")

