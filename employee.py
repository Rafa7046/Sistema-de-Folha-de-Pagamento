import random

employees = []
Id_list = []

class Employee:

    def __init__(self, name, address, type, Id):
        self.name = name
        self.address = address
        self.type = type
        self.Id = Id

    def new_employee(name, address, type):
        Id = random.randint(1, 10000)
        while Id in Id_list:
            Id = random.randint(1, 10000)
        Id_list.append(Id)
        employees.append( Employee(name, address, type, Id) )

    def remove_employee(reference):
        if type(reference) == int:
            to_remove = next((employee for employee in employees if employee.Id == reference), None )
        else:
            to_remove = next((employee for employee in employees if employee.name == reference), None )

        if to_remove == None:
            print("Esse funcionário não existe")
        else:
            employees.remove(to_remove)

    def print_data(self):
        print(f"O nome do empregrado é {self.name} \nMora no endereço {self.address} \nÉ do tipo {self.type} \nID = {self.Id}")

