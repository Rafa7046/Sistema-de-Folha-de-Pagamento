from utils import find_worker, generate_id
from employee import Employee, employees

def choice():
    option = input("")
    if option=="1" or option.lower == "adicionar um funcionário" or option.lower == "adicionar um funcionario":
        name = input("Digite o nome do funcionário: ")
        address = input("Digite o endereço do funcionário: ")
        type_of_worker = input("Digite o tipo do funcionário: ")
        type_of_payment = input("Digite o método de pagamento de sua preferência: ")
        print("================================================")
        employees.append(Employee(name, address, type_of_worker,type_of_payment, generate_id()))
    elif option=="2" or option.lower == "remover um funcionário" or option.lower == "remover um funcionario":
        removed = int(input("Digite o Id ou nome do funcionário que deseja remover: "))
        Employee.remove_employee(removed)
        print("================================================")
    elif option == "3" or option.lower == "lançar cartão de ponto" or option.lower == "lançar cartão de pontos" or option.lower == "lancar cartao de ponto" or option.lower == "lancar cartao de pontos":
        Id = int(input("Digite o Id do funcionário: "))
        hours_worked = int(input("O funcionário trbalhou por quantas horas: "))
        find_worker(Id, employees).type_of_worker.time_cards(hours_worked)
        print(f"Foi batido o ponto do funcionário {find_worker(Id, employees).name} com {hours_worked} de trabalho")
    elif option == "4" or option.lower == "lançar um Resultado venda" or option.lower == "lancar um Resultado venda":
        Id = int(input("Digite o Id do funcionário: "))
        value = int(input("Qual foi o valor da venda: "))
        find_worker(Id, employees).type_of_worker.sell_results(value)
        print(f"Foi adicionado o valor da comissão ao funcionário {find_worker(Id, employees).name} com Id = {Id}")



def start():
    print("Selecione a opção desejada")
    print("[1] Adicionar um funcionário")
    print("[2] Remover um funcionário")
    print("[3] Lançar um cartão de ponto")
    print("[4] Lançar um Resultado Venda")
    choice()
