from employee import Employee

def choice():
    option = input("")
    if option=="1" or option.lower == "adicionar um funcionário" or option.lower == "adicionar um funcionario":
        name = input("Digite o nome do funcionário: ")
        address = input("Digite o endereço do funcionário: ")
        type = input("Digite o tipo do funcionário: ")
        print("================================================")
        Employee.new_employee(name, address, type)
    elif option=="2" or option.lower == "remover um funcionário" or option.lower == "remover um funcionario":
        print("Digite o Id ou nome do funcionário que deseja remover: ")
        removed = input()
        Employee.remove_employee(removed)
        print("================================================")


def begining():
    print("Selecione a opção desejada")
    print("[1] Adicionar um funcionário")
    print("[2] Remover um funcionário")
    choice()
