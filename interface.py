from format import end_code, load_changes, save_object
from utils import find_worker, generate_id
from employee import Employee
from time_payments import avaliable_agendas, create_agenda, pay_employee

def choice(employees):
    var = 0
    option = input("")
    print("================================================")
    if option == "10":
        undo_redo = input("[0] Desfazer\n[1] Refazer\n ")
        if undo_redo == "0":
            save_object(employees, "data_backup.pkl")
            try:
                employees = load_changes("data.pkl")
            except:
                employees = []
            save_object(employees, "data.pkl")
        elif undo_redo == "1":
            employees = load_changes("data_backup.pkl")
            var = 1
        return employees, var
    elif option == "0" or option == "9" or len(employees) == 0:
        pass
    else:
        save_object(employees, "data.pkl")
    if option=="1" or option.lower() == "adicionar um funcionário" or option.lower() == "adicionar um funcionario":
        name = input("Digite o nome do funcionário: ")
        address = input("Digite o endereço do funcionário: ")
        type_of_worker = input("Digite o tipo do funcionário: ")
        type_of_payment = input("Digite o método de pagamento de sua preferência: ")
        syndicate = input("O funcionário faz parte de sindicatos? [sim] [nao]\n")
        if syndicate.lower() == "sim":
            syndicate = True
        else:
            syndicate = False
        employees.append(Employee(name, address, type_of_worker,type_of_payment, syndicate, generate_id()))
    elif option=="2" or option.lower() == "remover um funcionário" or option.lower() == "remover um funcionario":
        removed = int(input("Digite o Id ou nome do funcionário que deseja remover: "))
        Employee.remove_employee(removed, employees)
    elif option == "3" or option.lower() == "lançar cartão de ponto" or option.lower() == "lançar cartão de pontos" or option.lower() == "lancar cartao de ponto" or option.lower() == "lancar cartao de pontos":
        Id = int(input("Digite o Id do funcionário: "))
        hours_worked = int(input("O funcionário trbalhou por quantas horas: "))
        find_worker(Id, employees).type_of_worker.time_cards(hours_worked)
        print(f"Foi batido o ponto do funcionário {find_worker(Id, employees).name} com {hours_worked} de trabalho")
    elif option == "4" or option.lower() == "lançar um resultado venda" or option.lower() == "lancar um resultado venda":
        Id = int(input("Digite o Id do funcionário: "))
        value = int(input("Qual foi o valor da venda: "))
        find_worker(Id, employees).type_of_worker.sell_results(value)
        print(f"Foi adicionado o valor da comissão ao funcionário {find_worker(Id, employees).name} com Id = {Id}")
    elif option == "5" or option.lower() == "lançar uma taxa de serviço" or option == "lancar uma taxa de servico":
        Id = int(input("Digite o Id do funcionário: "))
        value = int(input("Qual foi o valor da taxa: "))
        find_worker(Id, employees).syndicate.service_fee(value)
        print(f"Foi adicionado o valor da taxa de serviço ao funcionário {find_worker(Id, employees).name} com Id = {Id}")
    elif option == "6" or option.lower() == "alterar detalhes de um empregado":
        Id = int(input("Digite o Id do funcionário: "))
        find_worker(Id, employees).edit_info()
        find_worker(Id, employees).print_data()
    elif option == "7" or option.lower() == "rodar a folha de pagamento para hoje":
        day, month, year = input("Qual o data para rodar a folhar? DD/MM/YYYY\n").split()
        pay_employee(employees, int(day), int(month), int(year))
    elif option == "0" or option.lower == "ver informacoes dos funcionarios":
        if len(employees) == 0:
            print("Não há nenhum funcionário")
        else:
            for x in employees:
                x.print_data()
    elif option == "8" or option.lower == "alterar agenda de pagamento":
        Id = int(input("Digite o Id do funcionário: "))
        print("Estão disponíveis as seguintes agendas de pagamento: ")
        print("Digite o número respectivo a agenda desejada.")
        new_agenda = avaliable_agendas()
        find_worker(Id, employees).type_of_worker.payment_agenda = new_agenda
        print(f"Foi alterado a agenda de pagamento do funcionário {Id} para {new_agenda}")
    elif option == "9" or option.lower == "criar agenda de pagamento":
        create_agenda()
        print("A nova agenda foi criada e já está disponível para ser escolhida")
    elif option == "-1" or option.lower == "sair":
        print("\n Sistema encerrado")
        end_code()
        exit()
    print("================================================ \n\n")
    return employees, var

def start(employees):
    print("Selecione a opção desjeada")
    print("[0] Ver informações dos funcionários")
    print("[1] Adicionar um funcionário")
    print("[2] Remover um funcionário")
    print("[3] Lançar um cartão de ponto")
    print("[4] Lançar um Resultado Venda")
    print("[5] Lançar uma taxa de serviço")
    print("[6] Alterar detalhes de um empregado")
    print("[7] Rodar a folha de pagamento")
    print("[8] Alterar agenda de pagamento")
    print("[9] Criar agenda de pagamento")
    print("[10] Desfazer ou refazer")
    print("[-1] Sair")
    employees, var = choice(employees)
    return employees, var
