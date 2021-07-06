from utils import find_worker, generate_id
from employee import Employee, employees

def choice():
    option = input("")
    if option=="1" or option.lower == "adicionar um funcionário" or option.lower == "adicionar um funcionario":
        name = input("Digite o nome do funcionário: ")
        address = input("Digite o endereço do funcionário: ")
        type_of_worker = input("Digite o tipo do funcionário: ")
        print("================================================")
        employees.append(Employee(name, address, type_of_worker, generate_id()))
    elif option=="2" or option.lower == "remover um funcionário" or option.lower == "remover um funcionario":
        removed = int(input("Digite o Id ou nome do funcionário que deseja remover: "))
        Employee.remove_employee(removed)
        print("================================================")
    elif option == "3" or option.lower == "lançar cartão de ponto" or option.lower == "lançar cartão de pontos" or option.lower == "lancar cartao de ponto" or option.lower == "lancar cartao de pontos":
        Id = int(input("Digite o Id do funcionário: "))
        hours_worked = int(input("O funcionário trbalhou por quantas horas: "))
        find_worker(Id, employees).type_of_worker.time_cards(hours_worked)


def start():
    print("Selecione a opção desejada")
    print("[1] Adicionar um funcionário")
    print("[2] Remover um funcionário")
    print("[3] Lançar um cartão de ponto")
    choice()
